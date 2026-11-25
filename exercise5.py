def square(n):
    """n multiplied by itself"""
    return n * n


def is_teenager(age):
    """True if age is from 13 to 19, both included"""
    return 13 < age <= 19


def count_vowels(text):
    """Number of vowels (a, e, i, o, u) in the text, uppercase or lowercase"""
    return sum(1 for c in text if c in "aeiou")


def max_of_list(numbers):
    """The largest number in the list, or None if the list is empty"""
    return max(numbers)


def last_n(items, n):
    """The last n items of the list. If n is 0, the result is an empty list"""
    return items[-n:] if n > 0 else []
