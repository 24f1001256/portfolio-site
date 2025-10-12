import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_mixed_numbers():
    assert longest_positive_streak([1, 2, -1, 4, 5, 6]) == 3

def test_streak_at_beginning():
    assert longest_positive_streak([1, 2, 3, -1, 0, 5]) == 3

def test_streak_at_end():
    assert longest_positive_streak([-1, 0, 5, 1, 2, 3]) == 4

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1]) == 3

def test_single_positive():
    assert longest_positive_streak([-1, -2, 5, -3, -4]) == 1

def test_zeros_in_list():
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6, 7]) == 4

def test_no_positive_numbers():
    assert longest_positive_streak([0, -1, -2, -3]) == 0