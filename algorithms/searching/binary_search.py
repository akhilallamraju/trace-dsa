"""Step-by-step Binary Search implementation."""

from collections.abc import Iterator, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class BinarySearchStep:
    """State of Binary Search immediately after a comparison."""

    low: int
    high: int
    mid: int | None
    comparisons: int
    found_index: int | None
    complete: bool


def binary_search_steps(
    values: Sequence[object],
    target: object,
) -> Iterator[BinarySearchStep]:
    """Yield each comparison state for an ascending, already-sorted sequence.

    The low/high values describe the range before the current comparison.
    The input is not modified or sorted automatically.
    """
    low = 0
    high = len(values) - 1
    comparisons = 0

    if not values:
        yield BinarySearchStep(0, -1, None, 0, None, True)
        return

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        value = values[mid]

        if value == target:
            yield BinarySearchStep(
                low, high, mid, comparisons, mid, True
            )
            return

        if target < value:
            next_low, next_high = low, mid - 1
        else:
            next_low, next_high = mid + 1, high

        complete = next_low > next_high
        yield BinarySearchStep(
            low, high, mid, comparisons, None, complete
        )

        if complete:
            return

        low, high = next_low, next_high
