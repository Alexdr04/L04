# Bug reports for exercise5.py

Line: 3
Problem: square returns n multiplied by 2, but the docstring says "n multiplied by itself".
Example: square(5) returns 10, expected 25.
Fix:     return n * n

Line: 8
Problem: is_teenager returns False for age 13, but the docstring says "from 13 to 19, both included".
Example: is_teenager(13) returns False, expected True.
Fix:     return 13 <= age <= 19

Line: 23
Problem: last_n returns items[-n:] when n is 0, which would be an empty list, but if n is larger than the list length, it returns an empty list, which is correct. However, if n is negative, it will raise an IndexError. The docstring does not specify behavior for negative n, and it's not covered. But since the docstring says "If n is 0, the result is an empty list", and doesn't mention negative n, and negative n is not a case mentioned, we must check if negative n is handled. The function currently raises an error for negative n, which is not specified. However, the docstring does not cover negative n, so it's not a bug unless negative n is a valid input. Since the docstring does not specify behavior for negative n, and the function fails, this is a missing specification. But the instruction says to check every case the docstring names. The docstring only mentions n=0. So negative n is not covered. But the bug is not in the docstring, it's in the function's behavior for invalid inputs. However, the instruction says to report only if the docstring names a case. Since negative n is not named, it's not a bug. So no bug here.

No other bugs found.
