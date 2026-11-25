import os
import sqlite3
import subprocess

import pytest

import exercise5
from exercise5 import *


# bug report 1
def test_r1_square_n_multiplied_by_itself():
    assert square(5) == 25


# bug report 2
def test_r2_is_teenager_age_13():  
    assert is_teenager(13) == True


# bug report 3
def test_r3_last_n_negative_n(): 
    assert last_n([1, 2, 3], -1) == []
