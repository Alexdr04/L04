# Bug reports for exercise3.py

Line: 3
Problem: average raises a ZeroDivisionError when the list is empty, but the docstring says an empty list has average 0.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix:     if len(numbers) == 0: return 0
        return sum(numbers) / len(numbers)

Line: 8
Problem: first_word returns the first word, but if the text has no words (e.g., empty string or only whitespace), it returns an empty string, which is correct per the docstring. However, if the text contains only whitespace, split() returns an empty list, and [0] will raise an IndexError. The docstring says "or "" if the text is empty", but whitespace is not empty.
Example: first_word("   ") returns '' (correct), but first_word("   ") should be handled safely — actually, split() on whitespace returns empty list, so [0] fails.
Fix:     words = text.split()
        if not words:
            return ""
        return words[0]

Line: 13
Problem: percent raises a ZeroDivisionError when total is 0, but the docstring says "If total is 0, the result is 0".
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix:     if total == 0: return 0
        return part / total * 100
