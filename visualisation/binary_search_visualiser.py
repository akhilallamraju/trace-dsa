"""Array visualiser for Binary Search."""

from visualisation.array_visualiser import ArrayVisualiser


class BinarySearchVisualiser(ArrayVisualiser):
    """Highlight the midpoint while retaining the shared array styling."""

    def __init__(self, parent, values=None, height=190):
        self.active_low = None
        self.active_high = None
        super().__init__(parent, values=values, height=height)

    def render_range(self, low, high, mid, found_index=None):
        """Render a midpoint and retain the current inclusive search bounds."""
        self.active_low = low
        self.active_high = high
        self.render(current_index=mid, found_index=found_index)

    def reset_highlights(self):
        self.active_low = None
        self.active_high = None
        super().reset_highlights()
