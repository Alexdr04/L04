# Bug reports for exercise4.py

Line: 4
Problem: The ADMIN_PASSWORD is hardcoded in the source code, making it vulnerable to exposure and easy to guess or compromise, which is a serious security risk.
Example: None
Fix: (No fix needed; this is a security issue, not a bug in logic)

Line: 9
Problem: The function returns True if the password is not equal to ADMIN_PASSWORD, which contradicts the docstring that says "true if the password is the admin password".
Example: check_admin("admin123") returns False, expected True.
Fix:     return ADMIN_PASSWORD == password

Line: 14
Problem: The SQL query is vulnerable to SQL injection because it directly interpolates the username into the query without escaping.
Example: find_user(db, "'; DROP TABLE users; --") returns a malicious result, potentially deleting the users table.
Fix:     return db.execute(f"SELECT * FROM users WHERE username = ?", (username,)).fetchone()
