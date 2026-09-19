import pytest

from tasks.strings_lists.tasks import (
    capitalize_words,
    char_freq,
    common,
    count_words,
    dedup,
    longest_word,
    remove_vowels,
    second_max,
    sum_numbers,
    top_k,
)


@pytest.mark.parametrize("s, expected", [
    ("одно два три", 3),
    ("  a   b  ", 2),
    ("слово", 1),
    ("", 0),
    ("   ", 0),
])
def test_count_words(s, expected):
    assert count_words(s) == expected


@pytest.mark.parametrize("s, expected", [
    ("ab12cd3", 15),
    ("100 и 200", 300),
    ("нет цифр", 0),
    ("7", 7),
    ("", 0),
    ("1a2a3", 6),
])
def test_sum_numbers(s, expected):
    assert sum_numbers(s) == expected


@pytest.mark.parametrize("s, expected", [
    ("Hello", "Hll"),
    ("привет", "првт"),
    ("xyz", "xyz"),
    ("", ""),
    ("AEIOU", ""),
])
def test_remove_vowels(s, expected):
    assert remove_vowels(s) == expected


@pytest.mark.parametrize("s, expected", [
    ("мама мыла раму", "мама"),
    ("a bb ccc", "ccc"),
    ("аб вг", "аб"),
    ("одно", "одно"),
    ("", ""),
])
def test_longest_word(s, expected):
    assert longest_word(s) == expected


@pytest.mark.parametrize("s, expected", [
    ("мама мыла раму", "Мама Мыла Раму"),
    ("  hi   there ", "Hi There"),
    ("ВСЁ КАПСОМ", "Всё Капсом"),
    ("", ""),
])
def test_capitalize_words(s, expected):
    assert capitalize_words(s) == expected


@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 4, 1, 5], 4),
    ([5, 5, 3], 3),
    ([2, 2], None),
    ([1], None),
    ([], None),
    ([-1, -2], -2),
])
def test_second_max(nums, expected):
    assert second_max(nums) == expected


@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 3, 2, 1], [3, 1, 2]),
    ([7, 7, 7], [7]),
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
])
def test_dedup(nums, expected):
    assert dedup(nums) == expected


@pytest.mark.parametrize("s, expected", [
    ("aab", {"a": 2, "b": 1}),
    ("a b", {"a": 1, "b": 1}),
    ("", {}),
    ("   ", {}),
    ("aA", {"a": 1, "A": 1}),
])
def test_char_freq(s, expected):
    assert char_freq(s) == expected


@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 3], [2, 3, 4], [2, 3]),
    ([1], [2], []),
    ([1, 1, 2], [2, 2], [2]),
    ([], [1, 2], []),
])
def test_common(a, b, expected):
    assert common(a, b) == expected


@pytest.mark.parametrize("nums, k, expected", [
    ([3, 1, 4, 1, 5], 2, [5, 4]),
    ([2, 2, 2], 2, [2, 2]),
    ([5], 1, [5]),
    ([1, 2, 3], 0, []),
    ([1, 2], 5, [2, 1]),
])
def test_top_k(nums, k, expected):
    assert top_k(nums, k) == expected
