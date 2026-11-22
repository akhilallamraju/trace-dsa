"""Tests for the step-by-step Binary Search implementation."""

from algorithms.searching.binary_search import (
    BinarySearchStep,
    binary_search_steps,
)


def test_finds_target_at_first_index():
    steps = list(binary_search_steps([2, 4, 6, 8, 10], 2))
    assert steps[-1] == BinarySearchStep(0, 1, 0, 2, 0, True)


def test_finds_target_in_middle():
    assert list(binary_search_steps([2, 4, 6, 8, 10], 6)) == [
        BinarySearchStep(0, 4, 2, 1, 2, True)
    ]


def test_finds_target_at_last_index():
    steps = list(binary_search_steps([2, 4, 6, 8, 10], 10))
    assert steps[-1].found_index == 4
    assert steps[-1].comparisons == 3
    assert steps[-1].complete


def test_reports_target_not_found():
    steps = list(binary_search_steps([2, 4, 6, 8, 10], 7))
    assert [step.mid for step in steps] == [2, 3]
    assert [step.comparisons for step in steps] == [1, 2]
    assert steps[-1].found_index is None
    assert steps[-1].complete


def test_handles_empty_sequence():
    assert list(binary_search_steps([], 7)) == [
        BinarySearchStep(0, -1, None, 0, None, True)
    ]


def test_handles_single_element_sequence():
    assert list(binary_search_steps([7], 7)) == [
        BinarySearchStep(0, 0, 0, 1, 0, True)
    ]


def test_does_not_modify_input_sequence():
    values = [2, 4, 6, 8, 10]
    original = values.copy()
    list(binary_search_steps(values, 8))
    assert values == original
