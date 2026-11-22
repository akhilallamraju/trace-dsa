"""Array visualiser for Binary Search, showing the active search interval."""

import tkinter as tk

import theme
from visualisation.array_visualiser import ArrayVisualiser


class BinarySearchVisualiser(ArrayVisualiser):
    """Highlight the midpoint and dim values outside the active range."""

    def __init__(self, parent, values=None, height=190):
        self.active_low = None
        self.active_high = None
        super().__init__(parent, values=values, height=height)

    def render_range(self, low, high, mid, found_index=None):
        self.active_low = low
        self.active_high = high
        self.current_index = mid
        self.found_index = found_index
        self._draw_array()

    def reset_highlights(self):
        self.active_low = None
        self.active_high = None
        super().reset_highlights()

    def _draw_array(self):
        self.canvas.delete("all")
        if not self.values:
            width = max(self.canvas.winfo_width(), 1)
            self.canvas.configure(scrollregion=(0, 0, width, self.canvas_height))
            self.canvas.create_text(
                width / 2, self.canvas_height / 2,
                text="Generate an array to get started",
                fill=theme.MUTED, font=theme.FONT_SUBTITLE,
            )
            return

        canvas_width = max(self.canvas.winfo_width(), 1)
        side_padding, gap, minimum_cell_width = 24, 8, 38
        available_width = max(canvas_width - 2 * side_padding, minimum_cell_width)
        cell_width = max(
            minimum_cell_width,
            min(72, (available_width - gap * (len(self.values) - 1)) // len(self.values)),
        )
        cell_height, index_label_height, top = 54, 24, 42
        total_width = (
            2 * side_padding + len(self.values) * cell_width
            + (len(self.values) - 1) * gap
        )

        for index, value in enumerate(self.values):
            left = side_padding + index * (cell_width + gap)
            right = left + cell_width
            bottom = top + cell_height
            in_range = (
                self.active_low is None
                or self.active_low <= index <= self.active_high
            )

            if index == self.found_index:
                fill, text_colour, outline = theme.GREEN, theme.BACKGROUND, theme.GREEN
            elif index == self.current_index:
                fill, text_colour, outline = theme.ORANGE, theme.BACKGROUND, theme.ORANGE
            elif in_range:
                fill, text_colour, outline = theme.SURFACE, theme.FOREGROUND, theme.MUTED
            else:
                fill, text_colour, outline = theme.BACKGROUND, theme.MUTED, theme.MUTED

            self.canvas.create_rectangle(
                left, top, right, bottom, fill=fill, outline=outline,
                width=2 if index in (self.current_index, self.found_index) else 1,
            )
            self.canvas.create_text(
                (left + right) / 2, top + cell_height / 2,
                text=str(value), fill=text_colour,
                font=(theme.FONT_FAMILY, 11, "bold"), width=cell_width - 6,
            )
            self.canvas.create_text(
                (left + right) / 2, bottom + index_label_height / 2,
                text=str(index), fill=theme.MUTED,
                font=theme.FONT_BUTTON_NUMBER,
            )

        self.canvas.configure(
            scrollregion=(0, 0, max(total_width, canvas_width), self.canvas_height)
        )
        self.canvas.xview_moveto(0)
