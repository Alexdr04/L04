# Bug reports for exercise5.py

Line: 3
Problem: square returns n multiplied by 2, but the docstring says "n multiplied by itself".
Example: square(3) returns 6, expected 9.
Fix:     return n * n

Line: 23
Problem: last_n returns items[-n:] when n is 0, which would cause an IndexError if the list is empty because negative indexing with 0 is invalid. It should return an empty list when n is 0.
Example: last_n([], 0) returns IndexError, expected [].
Fix:     return items[-n:] if n > 0 else []
