"""Задачи на строки и списки.

Реализуйте функции ниже. Запуск тестов:

    pytest -q

Пока функция не написана, её тесты падают — это нормально.
Решайте по одной и смотрите, как красное становится зелёным.
"""


def count_words(s: str) -> int:
    """Количество слов в строке.

    Слова разделены произвольным числом пробелов.
    Дополнительно: попробуйте решить без split(), одним проходом.

    Время: O(n), память: O(1)
    """
    raise NotImplementedError


def sum_numbers(s: str) -> int:
    """Сумма всех чисел в строке.

    Подряд идущие цифры образуют одно число: "ab12cd3" -> 12 + 3 = 15.

    Время: O(n), память: O(1)
    """
    raise NotImplementedError


def remove_vowels(s: str) -> str:
    """Строка без гласных букв. Регистр остальных символов сохраняется.

    Время: O(n), память: O(n)
    """
    raise NotImplementedError


def longest_word(s: str) -> str:
    """Самое длинное слово. Если таких несколько — первое из них.

    Для пустой строки вернуть пустую строку.

    Время: O(n), память: O(n)
    """
    raise NotImplementedError


def capitalize_words(s: str) -> str:
    """Каждое слово с заглавной буквы, остальные буквы строчные.

    Лишние пробелы убрать.

    Время: O(n), память: O(n)
    """
    raise NotImplementedError


def second_max(nums: list[int]) -> int | None:
    """Второе по величине РАЗЛИЧНОЕ значение или None, если его нет.

    Ограничение: один проход, без сортировки.

    Время: O(n), память: O(1)
    """
    raise NotImplementedError


def dedup(nums: list[int]) -> list[int]:
    """Список без повторов, порядок первых вхождений сохранён.

    Время: O(n), память: O(n)
    """
    raise NotImplementedError


def char_freq(s: str) -> dict[str, int]:
    """Частота символов. Пробелы не считаются.

    Ограничение: без collections.Counter.

    Время: O(n), память: O(k)
    """
    raise NotImplementedError


def common(a: list[int], b: list[int]) -> list[int]:
    """Отсортированный список значений, которые есть в обоих списках.

    Каждое значение — один раз.

    Время: O(n + m + k log k), память: O(n)
    """
    raise NotImplementedError


def top_k(nums: list[int], k: int) -> list[int]:
    """k наибольших значений по убыванию. Повторы сохраняются.

    Время: O(n log n), память: O(n)
    """
    raise NotImplementedError
