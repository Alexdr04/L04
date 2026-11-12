# Bug reports for exercise1.py

Line: 3
Problem: is_even returns True for odd numbers because it checks if n % 2 == 1, which is incorrect; it should return True for even numbers.
Example: is_even(4) returns False, expected True.
Fix:     return n % 2 == 0

Line: 8
Problem: rectangle_area returns the sum of width and height instead of the product, which is the correct formula for area.
Example: rectangle_area(5, 3) returns 8, expected 15.
Fix:     return width * height

Line: 13
Problem: double returns n + 2 instead of n * 2, which contradicts the docstring "twice the number n".
Example: double(5) returns 7, expected 10.
Fix:     return n * 2
