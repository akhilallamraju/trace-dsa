"""Reusable Canvas-based visualisation for array algorithms."""

import tkinter as tk

import theme


class ArrayVisualiser(tk.Frame):
    """Display an array and highlight the indices used by an algorithm.

    The component does not depend on a particular algorithm. Call
    set_values() when the array changes, then render() whenever an
    algorithm produces a new state.
    """

    def __init__(self, parent, values=None, height=190):
        super().__init__(parent, bg=theme.BACKGROUND)

        self.values = list(values) if values is not None else []
        self.current_index = None
        self.found_index = None
        self.canvas_height = height

        self.canvas = tk.Canvas(
            self,
            height=height,
            bg=theme.BACKGROUND,
            highlightthickness=0,
            borderwidth=0,
        )
        self.scrollbar = tk.Scrollbar(
            self,
            orient="horizontal",
            command=self.canvas.xview,
        )
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas.pack(fill="both", expand=True)
        self.scrollbar.pack(fill="x")

        self.canvas.bind("<Configure>", self._on_canvas_resize)

        self._draw_array()

    def set_values(self, values):
        """Replace the displayed values and clear any previous highlights."""
        self.values = list(values)
        self.current_index = None
        self.found_index = None
        self._draw_array()

    def render(self, current_index=None, found_index=None):
        """Redraw the array with the supplied algorithm state.

        Args:
            current_index: Index currently being inspected, if any.
            found_index: Index where the target was found, if any.
        """
        self.current_index = current_index
        self.found_index = found_index
        self._draw_array()

    def reset_highlights(self):
        """Remove current and found highlights without changing the array."""
        self.render()

    def _on_canvas_resize(self, _event):
        self._draw_array()

    def _draw_array(self):
        self.canvas.delete("all")

        if not self.values:
            self.canvas.configure(
                scrollregion=(0, 0, max(self.canvas.winfo_width(), 1), self.canvas_height)
            )
            self.canvas.create_text(
                max(self.canvas.winfo_width(), 1) / 2,
                self.canvas_height / 2,
                text="Generate an array to get started",
                fill=theme.MUTED,
                font=theme.FONT_SUBTITLE,
            )
            return

        canvas_width = max(self.canvas.winfo_width(), 1)
        side_padding = 24
        gap = 8
        minimum_cell_width = 38
        available_width = max(canvas_width - 2 * side_padding, minimum_cell_width)

        # Fit cells to the visible canvas where possible. For larger arrays,
        # keep a readable minimum width and let the horizontal scrollbar help.
        cell_width = max(
            minimum_cell_width,
            min(72, (available_width - gap * (len(self.values) - 1)) // len(self.values)),
        )
        cell_height = 54
        index_label_height = 24
        top = 42
        total_width = (
            2 * side_padding
            + len(self.values) * cell_width
            + (len(self.values) - 1) * gap
        )

        for index, value in enumerate(self.values):
            left = side_padding + index * (cell_width + gap)
            right = left + cell_width
            bottom = top + cell_height

            if index == self.found_index:
                fill = theme.GREEN
                text_colour = theme.BACKGROUND
                outline = theme.GREEN
            elif index == self.current_index:
                fill = theme.ORANGE
                text_colour = theme.BACKGROUND
                outline = theme.ORANGE
            else:
                fill = theme.SURFACE
                text_colour = theme.FOREGROUND
                outline = theme.MUTED

            self.canvas.create_rectangle(
                left,
                top,
                right,
                bottom,
                fill=fill,
                outline=outline,
                width=2 if index in (self.current_index, self.found_index) else 1,
            )
            self.canvas.create_text(
                (left + right) / 2,
                top + cell_height / 2,
                text=str(value),
                fill=text_colour,
                font=(theme.FONT_FAMILY, 11, "bold"),
                width=cell_width - 6,
            )
            self.canvas.create_text(
                (left + right) / 2,
                bottom + index_label_height / 2,
                text=str(index),
                fill=theme.MUTED,
                font=theme.FONT_BUTTON_NUMBER,
            )

        self.canvas.configure(
            scrollregion=(0, 0, max(total_width, canvas_width), self.canvas_height)
        )
