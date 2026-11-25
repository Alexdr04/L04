import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin_hardcoded_password():
    assert check_admin("admin123") == False


# bug report 2
def test_r2_find_user_sql_injection():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, password TEXT)")
    db.execute("INSERT INTO users VALUES ('alice', 'password123')")
    assert find_user(db, "'; DROP TABLE users; --") == None
