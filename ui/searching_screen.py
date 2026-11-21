"""Interactive Linear Search screen for Trace."""

import random
import tkinter as tk
from tkinter import messagebox

import theme
from algorithms.searching.linear_search import linear_search_steps
from visualisation.array_visualiser import ArrayVisualiser


class SearchingScreen(tk.Frame):
    """Provide an animated, interactive Linear Search demonstration."""

    ARRAY_SIZE = 10
    MIN_VALUE = 1
    MAX_VALUE = 99
    ANIMATION_DELAY_MS = 650

    def __init__(self, parent, back_callback):
        super().__init__(parent, bg=theme.BACKGROUND)
        self.back_callback = back_callback

        self.values = []
        self.search_generator = None
        self.after_id = None
        self.is_running = False

        self._build_layout()
        self.generate_array()

    def _build_layout(self):
        header = tk.Frame(self, bg=theme.BACKGROUND)
        header.pack(fill="x", padx=theme.PADDING, pady=(16, 4))

        back_button = tk.Button(
            header,
            text="← Back to Searching",
            command=self.back_callback,
            font=theme.FONT_BUTTON_DESCRIPTION,
            fg=theme.FOREGROUND,
            bg=theme.SURFACE,
            activebackground=theme.SURFACE_HOVER,
            activeforeground=theme.FOREGROUND,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=7,
        )
        back_button.pack(side="left")

        heading = tk.Frame(self, bg=theme.BACKGROUND)
        heading.pack(fill="x", padx=theme.PADDING, pady=(8, 14))

        tk.Label(
            heading,
            text="Linear Search",
            font=theme.FONT_TITLE,
            fg=theme.CYAN,
            bg=theme.BACKGROUND,
        ).pack(anchor="w")

        tk.Label(
            heading,
            text="Check each element in sequence until the target is found.",
            font=theme.FONT_SUBTITLE,
            fg=theme.MUTED,
            bg=theme.BACKGROUND,
        ).pack(anchor="w", pady=(2, 0))

        self.visualiser = ArrayVisualiser(self, height=175)
        self.visualiser.pack(fill="x", padx=theme.PADDING, pady=(0, 12))

        controls = tk.Frame(self, bg=theme.BACKGROUND)
        controls.pack(fill="x", padx=theme.PADDING, pady=4)

        target_panel = tk.Frame(controls, bg=theme.BACKGROUND)
        target_panel.pack(side="left", fill="y")

        tk.Label(
            target_panel,
            text="TARGET VALUE",
            font=theme.FONT_BUTTON_NUMBER,
            fg=theme.MUTED,
            bg=theme.BACKGROUND,
        ).pack(anchor="w", pady=(0, 5))

        self.target_entry = tk.Entry(
            target_panel,
            width=12,
            font=(theme.FONT_FAMILY, 13),
            fg=theme.FOREGROUND,
            bg=theme.SURFACE,
            insertbackground=theme.FOREGROUND,
            relief="flat",
            justify="center",
        )
        self.target_entry.pack(ipady=7)
        self.target_entry.bind("<Return>", lambda _event: self.start_search())

        button_panel = tk.Frame(controls, bg=theme.BACKGROUND)
        button_panel.pack(side="right", anchor="s")

        self.generate_button = self._make_button(
            button_panel, "Generate Array", self.generate_array, theme.SURFACE
        )
        self.generate_button.pack(side="left", padx=(0, 7))

        self.start_button = self._make_button(
            button_panel, "Start Search", self.start_search, theme.GREEN,
            foreground=theme.BACKGROUND,
        )
        self.start_button.pack(side="left", padx=(0, 7))

        self.reset_button = self._make_button(
            button_panel, "Reset", self.reset_search, theme.SURFACE
        )
        self.reset_button.pack(side="left")

        info = tk.Frame(self, bg=theme.SURFACE, padx=16, pady=12)
        info.pack(fill="x", padx=theme.PADDING, pady=(18, 8))

        stats = tk.Frame(info, bg=theme.SURFACE)
        stats.pack(fill="x")

        self.comparisons_value = self._make_stat(stats, "COMPARISONS", "0")
        self.comparisons_value.pack(side="left", expand=True, anchor="w")

        self.index_value = self._make_stat(stats, "CURRENT INDEX", "—")
        self.index_value.pack(side="left", expand=True, anchor="w")

        self.result_value = self._make_stat(stats, "RESULT", "Not started")
        self.result_value.pack(side="left", expand=True, anchor="w")

        self.status_label = tk.Label(
            self,
            text="Generate an array, enter a target and start searching.",
            font=theme.FONT_SUBTITLE,
            fg=theme.MUTED,
            bg=theme.BACKGROUND,
            anchor="w",
            wraplength=900,
            justify="left",
        )
        self.status_label.pack(fill="x", padx=theme.PADDING, pady=(8, 0))

        legend = tk.Frame(self, bg=theme.BACKGROUND)
        legend.pack(fill="x", padx=theme.PADDING, pady=(10, 0))

        self._make_legend_item(legend, theme.ORANGE, "Current element").pack(
            side="left", padx=(0, 18)
        )
        self._make_legend_item(legend, theme.GREEN, "Target found").pack(side="left")

        tk.Label(
            self,
            text="TRACE | DATA STRUCTURES & ALGORITHMS",
            font=theme.FONT_FOOTER,
            fg=theme.MUTED,
            bg=theme.BACKGROUND,
        ).pack(side="bottom", pady=12)

    @staticmethod
    def _make_button(parent, text, command, background, foreground=None):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=theme.FONT_BUTTON_DESCRIPTION,
            fg=foreground or theme.FOREGROUND,
            bg=background,
            activeforeground=foreground or theme.FOREGROUND,
            activebackground=theme.SURFACE_HOVER,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=9,
        )

    @staticmethod
    def _make_stat(parent, label, initial_value):
        panel = tk.Frame(parent, bg=theme.SURFACE)
        tk.Label(
            panel,
            text=label,
            font=theme.FONT_BUTTON_NUMBER,
            fg=theme.MUTED,
            bg=theme.SURFACE,
        ).pack(anchor="w")
        value = tk.Label(
            panel,
            text=initial_value,
            font=(theme.FONT_FAMILY, 17, "bold"),
            fg=theme.FOREGROUND,
            bg=theme.SURFACE,
        )
        value.pack(anchor="w", pady=(3, 0))
        panel.value_label = value
        return panel

    @staticmethod
    def _make_legend_item(parent, colour, text):
        item = tk.Frame(parent, bg=theme.BACKGROUND)
        swatch = tk.Canvas(
            item, width=12, height=12, bg=theme.BACKGROUND,
            highlightthickness=0,
        )
        swatch.create_rectangle(1, 1, 11, 11, fill=colour, outline=colour)
        swatch.pack(side="left", padx=(0, 6))
        tk.Label(
            item, text=text, font=theme.FONT_BUTTON_DESCRIPTION,
            fg=theme.MUTED, bg=theme.BACKGROUND,
        ).pack(side="left")
        return item

    def _set_stat(self, panel, value):
        panel.value_label.configure(text=str(value))

    def _cancel_animation(self):
        if self.after_id is not None:
            try:
                self.after_cancel(self.after_id)
            except tk.TclError:
                pass
            self.after_id = None
        self.is_running = False
        self.search_generator = None

    def generate_array(self):
        """Create a new random array and clear the previous search."""
        self._cancel_animation()
        self.values = [
            random.randint(self.MIN_VALUE, self.MAX_VALUE)
            for _ in range(self.ARRAY_SIZE)
        ]
        self.visualiser.set_values(self.values)
        self.target_entry.delete(0, tk.END)
        self._set_stat(self.comparisons_value, 0)
        self._set_stat(self.index_value, "—")
        self._set_stat(self.result_value, "Not started")
        self.status_label.configure(
            text="New array generated. Enter a target value and start searching.",
            fg=theme.MUTED,
        )
        self._set_controls_running(False)

    def start_search(self):
        """Validate the target and begin stepping through Linear Search."""
        if self.is_running:
            return

        raw_target = self.target_entry.get().strip()
        try:
            target = int(raw_target)
        except ValueError:
            messagebox.showerror(
                "Invalid target",
                "Please enter a whole number to search for.",
                parent=self,
            )
            self.target_entry.focus_set()
            return

        if not self.values:
            self.status_label.configure(text="Generate an array before searching.")
            return

        self._cancel_animation()
        self.visualiser.reset_highlights()
        self._set_stat(self.comparisons_value, 0)
        self._set_stat(self.index_value, "—")
        self._set_stat(self.result_value, "Searching")
        self.status_label.configure(
            text=f"Searching for {target}...",
            fg=theme.CYAN,
        )

        self.search_generator = linear_search_steps(self.values, target)
        self.is_running = True
        self._set_controls_running(True)
        self.after_id = self.after(250, self._advance_search)

    def _advance_search(self):
        """Consume one algorithm state and schedule the next animation frame."""
        self.after_id = None
        if not self.is_running or self.search_generator is None:
            return

        try:
            step = next(self.search_generator)
        except StopIteration:
            self._finish_search_without_result()
            return

        self.visualiser.render(
            current_index=step.current_index,
            found_index=step.found_index,
        )
        self._set_stat(self.comparisons_value, step.comparisons)
        self._set_stat(
            self.index_value,
            step.current_index if step.current_index is not None else "—",
        )

        if step.complete:
            self._finish_search(step.found_index, step.comparisons)
            return

        self.status_label.configure(
            text=f"Checking index {step.current_index}: "
                 f"{self.values[step.current_index]} does not match.",
            fg=theme.ORANGE,
        )
        self.after_id = self.after(
            self.ANIMATION_DELAY_MS, self._advance_search
        )

    def _finish_search(self, found_index, comparisons):
        self.is_running = False
        self.search_generator = None
        self.after_id = None
        self._set_controls_running(False)

        if found_index is not None:
            self._set_stat(self.result_value, f"Found at {found_index}")
            self.status_label.configure(
                text=f"Found the target at index {found_index} "
                     f"after {comparisons} comparison(s).",
                fg=theme.GREEN,
            )
        else:
            self._set_stat(self.result_value, "Not found")
            self.status_label.configure(
                text=f"Target not found after checking all "
                     f"{comparisons} element(s).",
                fg=theme.PINK,
            )

    def _finish_search_without_result(self):
        self.is_running = False
        self.search_generator = None
        self._set_controls_running(False)
        self._set_stat(self.result_value, "Not found")
        self.status_label.configure(
            text="The array is empty; there were no elements to compare.",
            fg=theme.PINK,
        )

    def reset_search(self):
        """Stop an active search and restore the current array to its initial state."""
        self._cancel_animation()
        self.visualiser.reset_highlights()
        self._set_stat(self.comparisons_value, 0)
        self._set_stat(self.index_value, "—")
        self._set_stat(self.result_value, "Not started")
        self.status_label.configure(
            text="Search reset. You can run it again with the same array.",
            fg=theme.MUTED,
        )
        self._set_controls_running(False)

    def _set_controls_running(self, running):
        state = tk.DISABLED if running else tk.NORMAL
        self.start_button.configure(state=state)
        self.generate_button.configure(state=state)
        self.reset_button.configure(state=tk.NORMAL)
        self.target_entry.configure(state=state)

    def destroy(self):
        """Cancel scheduled callbacks before destroying the screen."""
        self._cancel_animation()
        super().destroy()
