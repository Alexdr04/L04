# Bug reports for exercise4.py

Line: 4
Problem: the ADMIN_PASSWORD is written in the code, so anyone who reads the code knows the admin password.
Example: check_admin("admin123") returns True, expected False.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 14
Problem: the function uses string formatting to build a SQL query without escaping, which makes it vulnerable to SQL injection.
Example: find_user(db, "'; DROP TABLE users; --") returns a row with the dropped table, expected None.
Fix:     return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
