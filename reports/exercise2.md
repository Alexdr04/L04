# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for a grade of exactly 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix:     return grade >= 5

Line: 8
Problem: is_valid_password does not check for at least 8 characters; it checks for more than 8, which means it fails for passwords exactly 8 characters long.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix:     return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: clamp incorrectly uses min(x, low) and then max(low, min(x, low)), which results in x being clamped to low regardless of high. It should clamp x to the range [low, high].
Example: clamp(10, 5, 15) returns 5, expected 10.
Fix:     return max(low, min(x, high))
