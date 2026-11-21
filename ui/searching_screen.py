"""Interactive Linear Search visualisation screen."""

import random
import tkinter as tk
from tkinter import messagebox

import theme
from algorithms.searching.linear_search import linear_search_steps
from visualisation.array_visualiser import ArrayVisualiser


class SearchingScreen(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg=theme.BACKGROUND)
        self.back_callback = back_callback
        self.values = []
        self._steps = None
        self._after_id = None
        self._running = False

        self._build_ui()
        self.generate_array()

    def _build_ui(self):
        header = tk.Frame(self, bg=theme.BACKGROUND)
        header.pack(fill="x", padx=32, pady=(22, 8))

        tk.Button(
            header, text="← Back to Searching", command=self._go_back,
            font=theme.FONT_SUBTITLE, fg=theme.CYAN, bg=theme.BACKGROUND,
            activebackground=theme.BACKGROUND, activeforeground=theme.FOREGROUND,
            relief="flat", bd=0, cursor="hand2",
        ).pack(side="left")

        tk.Label(
            header, text="Linear Search", font=theme.FONT_TITLE,
            fg=theme.GREEN, bg=theme.BACKGROUND,
        ).pack(pady=(12, 2))

        tk.Label(
            header, text="Explore how an array is searched one element at a time.",
            font=theme.FONT_SUBTITLE, fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack()

        controls = tk.Frame(self, bg=theme.BACKGROUND)
        controls.pack(fill="x", padx=42, pady=(22, 12))

        tk.Label(
            controls, text="TARGET", font=theme.FONT_BUTTON_NUMBER,
            fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(side="left", padx=(0, 8))

        self.target_entry = tk.Entry(
            controls, width=10, font=theme.FONT_BUTTON_TITLE,
            fg=theme.FOREGROUND, bg=theme.SURFACE, insertbackground=theme.FOREGROUND,
            relief="flat", justify="center",
        )
        self.target_entry.pack(side="left", ipady=7, padx=(0, 14))

        self.start_button = tk.Button(
            controls, text="▶  Start Search", command=self.start_search,
            font=theme.FONT_BUTTON_NUMBER, fg=theme.BACKGROUND, bg=theme.GREEN,
            activebackground=theme.CYAN, relief="flat", bd=0, cursor="hand2",
            padx=14, pady=8,
        )
        self.start_button.pack(side="left", padx=(0, 8))

        self.reset_button = tk.Button(
            controls, text="Reset", command=self.reset_search,
            font=theme.FONT_BUTTON_NUMBER, fg=theme.FOREGROUND, bg=theme.SURFACE,
            activebackground=theme.SURFACE_HOVER, relief="flat", bd=0,
            cursor="hand2", padx=14, pady=8,
        )
        self.reset_button.pack(side="left", padx=(0, 8))

        tk.Button(
            controls, text="↻  Generate Array", command=self.generate_array,
            font=theme.FONT_BUTTON_NUMBER, fg=theme.BACKGROUND, bg=theme.CYAN,
            activebackground=theme.GREEN, relief="flat", bd=0, cursor="hand2",
            padx=14, pady=8,
        ).pack(side="left")

        self.array_visualiser = ArrayVisualiser(self, height=190)
        self.array_visualiser.pack(fill="x", padx=34, pady=(8, 4))

        legend = tk.Frame(self, bg=theme.BACKGROUND)
        legend.pack(pady=(5, 12))
        self._legend_item(legend, theme.ORANGE, "Current")
        self._legend_item(legend, theme.GREEN, "Found")

        stats = tk.Frame(self, bg=theme.SURFACE)
        stats.pack(fill="x", padx=42, pady=(8, 0))

        self.comparisons_value = self._stat(stats, "COMPARISONS", "0")
        self.index_value = self._stat(stats, "CURRENT INDEX", "—")
        self.result_value = self._stat(stats, "RESULT", "Ready")

        self.status_label = tk.Label(
            self, text="Enter a target and start the search.",
            font=theme.FONT_SUBTITLE, fg=theme.MUTED, bg=theme.BACKGROUND,
        )
        self.status_label.pack(pady=(14, 0))

        tk.Label(
            self, text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER, fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(side="bottom", pady=16)

    def _legend_item(self, parent, colour, label):
        item = tk.Frame(parent, bg=theme.BACKGROUND)
        item.pack(side="left", padx=10)
        tk.Label(item, text="●", fg=colour, bg=theme.BACKGROUND).pack(side="left", padx=(0, 5))
        tk.Label(item, text=label, fg=theme.MUTED, bg=theme.BACKGROUND,
                 font=theme.FONT_BUTTON_DESCRIPTION).pack(side="left")

    def _stat(self, parent, label, initial):
        cell = tk.Frame(parent, bg=theme.SURFACE)
        cell.pack(side="left", expand=True, fill="x", padx=10, pady=12)
        tk.Label(cell, text=label, font=theme.FONT_BUTTON_NUMBER,
                 fg=theme.MUTED, bg=theme.SURFACE).pack()
        value = tk.Label(cell, text=initial, font=theme.FONT_BUTTON_TITLE,
                         fg=theme.FOREGROUND, bg=theme.SURFACE)
        value.pack(pady=(4, 0))
        return value

    def generate_array(self):
        self._stop_animation()
        self.values = [random.randint(1, 99) for _ in range(10)]
        self.array_visualiser.set_values(self.values)
        self.target_entry.delete(0, tk.END)
        self.comparisons_value.config(text="0")
        self.index_value.config(text="—")
        self.result_value.config(text="Ready", fg=theme.FOREGROUND)
        self.status_label.config(text="New array generated. Enter a target to begin.")
        self.start_button.config(state="normal")

    def start_search(self):
        if self._running:
            return
        raw_target = self.target_entry.get().strip()
        try:
            target = int(raw_target)
        except ValueError:
            messagebox.showerror("Invalid target", "Please enter a whole number.")
            self.target_entry.focus_set()
            return

        self._stop_animation()
        self.array_visualiser.reset_highlights()
        self.comparisons_value.config(text="0")
        self.index_value.config(text="—")
        self.result_value.config(text="Searching…", fg=theme.ORANGE)
        self.status_label.config(text=f"Searching for {target}…")
        self._steps = iter(linear_search_steps(self.values, target))
        self._running = True
        self.start_button.config(state="disabled")
        self._after_id = self.after(250, self._advance_search)

    def _advance_search(self):
        self._after_id = None
        if not self._running or self._steps is None:
            return
        try:
            step = next(self._steps)
        except StopIteration:
            self._finish_not_found()
            return

        self.comparisons_value.config(text=str(step.comparisons))
        self.index_value.config(
            text="—" if step.current_index is None else str(step.current_index)
        )
        self.array_visualiser.render(
            current_index=step.current_index,
            found_index=step.found_index,
        )

        if step.found_index is not None:
            self._running = False
            self.result_value.config(text=f"Found at {step.found_index}", fg=theme.GREEN)
            self.status_label.config(text="Target found. Linear Search is complete.")
            self.start_button.config(state="normal")
        elif step.complete:
            self._finish_not_found()
        else:
            self._after_id = self.after(650, self._advance_search)

    def _finish_not_found(self):
        self._running = False
        self._steps = None
        self.result_value.config(text="Not found", fg=theme.PINK)
        self.status_label.config(text="Target is not present in this array.")
        self.start_button.config(state="normal")

    def reset_search(self):
        self._stop_animation()
        self.array_visualiser.reset_highlights()
        self.comparisons_value.config(text="0")
        self.index_value.config(text="—")
        self.result_value.config(text="Ready", fg=theme.FOREGROUND)
        self.status_label.config(text="Search reset. Enter a target to begin.")
        self.start_button.config(state="normal")

    def _stop_animation(self):
        self._running = False
        self._steps = None
        if self._after_id is not None:
            try:
                self.after_cancel(self._after_id)
            except tk.TclError:
                pass
            self._after_id = None

    def _go_back(self):
        self._stop_animation()
        self.back_callback()

    def destroy(self):
        self._stop_animation()
        super().destroy()
