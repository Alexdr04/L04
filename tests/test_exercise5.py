import os
import sqlite3
import subprocess

import pytest

import exercise5
from exercise5 import *


# bug report 1
def test_r1_square_multipled_by_itself():  
    assert square(3) == 9


# bug report 2
def test_r2_last_n_zero_returns_empty_list():
    assert last_n([], 0) == []
