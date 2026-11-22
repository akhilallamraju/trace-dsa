"""Interactive Binary Search screen for Trace."""

import theme

from algorithms.searching.binary_search import binary_search_steps
from ui.searching_screen import SearchingScreen
from visualisation.binary_search_visualiser import BinarySearchVisualiser


class BinarySearchingScreen(SearchingScreen):
    """Reuse the Linear Search layout with sorted data and Binary Search steps."""

    TITLE = "Binary Search"
    SUBTITLE = "Repeatedly halve the sorted search range."
    VISUALISER_CLASS = BinarySearchVisualiser
    SORT_VALUES = True
    HEADING_COLOUR = theme.PURPLE

    def _create_search_generator(self, target):
        return binary_search_steps(self.values, target)

    def _advance_search(self):
        """Consume one Binary Search state and schedule the next animation frame."""
        self.after_id = None
        if not self.is_running or self.search_generator is None:
            return

        try:
            step = next(self.search_generator)
        except StopIteration:
            self._finish_search_without_result()
            return

        self.visualiser.render_range(
            low=step.low,
            high=step.high,
            mid=step.mid,
            found_index=step.found_index,
        )
        self._set_stat(self.comparisons_value, step.comparisons)
        self._set_stat(
            self.index_value,
            step.mid if step.mid is not None else "—",
        )

        if step.complete:
            self._finish_search(step.found_index, step.comparisons)
            return

        target = int(self.target_entry.get())
        if self.values[step.mid] < target:
            next_low, next_high = step.mid + 1, step.high
        else:
            next_low, next_high = step.low, step.mid - 1
        self.status_label.configure(
            text=(
                f"Checking midpoint at index {step.mid}: "
                f"{self.values[step.mid]}. "
                f"Next search range: {next_low}–{next_high}."
            ),
            fg=theme.ORANGE,
        )
        self.after_id = self.after(
            self.ANIMATION_DELAY_MS, self._advance_search
        )
