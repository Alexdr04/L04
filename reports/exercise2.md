# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for a grade of exactly 5, but the docstring says "True if the grade is 5 or more".
Example: is_passing(5) returns False, expected True.
Fix:     return grade >= 5

Line: 13
Problem: clamp incorrectly uses min(x, low) and then max(low, ...), which results in x being clamped to low regardless of high. It should clamp x to the range [low, high].
Example: clamp(3, 1, 10) returns 1, expected 3.
Fix:     return max(low, min(x, high))

Line: 8
Problem: is_valid_password does not check for at least one digit correctly; it uses any(c.isdigit() for c in password), which is correct, but the function fails to ensure the password has at least 8 characters and one digit. However, the logic is actually correct — the bug is in the docstring: it says "at least 8 characters and at least one digit", but the condition len(password) > 8 means it fails for exactly 8 characters. This is a mismatch.
Example: is_valid_password("abcdefgh1") returns False, expected True.
Fix:     return len(password) >= 8 and any(c.isdigit() for c in password)
