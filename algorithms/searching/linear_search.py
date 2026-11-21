"""Step-by-step Linear Search implementation.

The generator is independent of Tkinter so it can be tested on its own
and consumed by any visualisation layer.
"""

from collections.abc import Iterator, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class LinearSearchStep:
    """State of Linear Search immediately after a comparison."""

    current_index: int | None
    comparisons: int
    found_index: int | None
    complete: bool


def linear_search_steps(
    values: Sequence[object],
    target: object,
) -> Iterator[LinearSearchStep]:
    """Yield the state after each comparison made by Linear Search.

    The final yielded step has complete=True. For an empty sequence, one
    completed step is yielded with zero comparisons.

    Time complexity: O(n) worst case.
    Auxiliary space: O(1), excluding yielded step objects.
    """
    comparisons = 0

    for index, value in enumerate(values):
        comparisons += 1
        found = value == target
        is_last_value = index == len(values) - 1

        yield LinearSearchStep(
            current_index=index,
            comparisons=comparisons,
            found_index=index if found else None,
            complete=found or is_last_value,
        )

        if found:
            return

    if not values:
        yield LinearSearchStep(
            current_index=None,
            comparisons=0,
            found_index=None,
            complete=True,
        )
