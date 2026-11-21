"""Tests for the step-by-step Linear Search implementation."""

from algorithms.searching.linear_search import (
    LinearSearchStep,
    linear_search_steps,
)


def test_finds_target_at_first_index():
    steps = list(linear_search_steps([4, 8, 12], 4))

    assert steps == [
        LinearSearchStep(
            current_index=0,
            comparisons=1,
            found_index=0,
            complete=True,
        )
    ]


def test_finds_target_in_middle():
    steps = list(linear_search_steps([4, 8, 12, 16], 12))

    assert [step.current_index for step in steps] == [0, 1, 2]
    assert [step.comparisons for step in steps] == [1, 2, 3]
    assert steps[-1].found_index == 2
    assert steps[-1].complete is True


def test_finds_target_at_last_index():
    steps = list(linear_search_steps([4, 8, 12], 12))

    assert len(steps) == 3
    assert steps[-1].found_index == 2
    assert steps[-1].complete is True


def test_reports_target_not_found():
    steps = list(linear_search_steps([4, 8, 12], 99))

    assert len(steps) == 3
    assert steps[-1].current_index == 2
    assert steps[-1].comparisons == 3
    assert steps[-1].found_index is None
    assert steps[-1].complete is True


def test_handles_empty_sequence():
    steps = list(linear_search_steps([], 99))

    assert steps == [
        LinearSearchStep(
            current_index=None,
            comparisons=0,
            found_index=None,
            complete=True,
        )
    ]


def test_does_not_modify_input_sequence():
    values = [7, 2, 9]
    original = values.copy()

    list(linear_search_steps(values, 9))

    assert values == original
