import System
import pytest

def test_check_grades():
    database = System.System()
    database.login('akend3', '123454321')
    grades = database.usr.check_grades('databases')
    assert grades[0] == ['assignment1', 23]
    assert  grades[1] == ['assignment2', 46]