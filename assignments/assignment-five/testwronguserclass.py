import pytest
import System

def test_student_logging_in_with_TA_class (grade_system):
    grade_system.login ('akend3','123454321')
    assert grade_system.usr.users ['akend3']['role'] == 'TA'

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem