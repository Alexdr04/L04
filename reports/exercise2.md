# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for a grade of exactly 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix:     return grade >= 5

Line: 8
Problem: is_valid_password returns False for a password with exactly 8 characters, but the docstring says "at least 8".
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix:     return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: clamp returns low when x is less than or equal to low, but the function should return x if it's within the range [low, high]. The line uses min(x, low) which is incorrect; it should be min(x, high).
Example: clamp(3, 1, 10) returns 1, expected 3.
Fix:     return max(low, min(x, high))
