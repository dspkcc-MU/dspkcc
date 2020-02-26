import pytest
import System

def test_change_grade (grade_system):
	username = 'cmhbf5'
	password = 'bestTA'
	grade_system.login (username,password)
	
	grade_system.usr.change_grade('akend3', 'comp_sci', 'assignment1', 100)
	grade_system.reload_data()
	
	assert grade_system.usr.users['akend3']['courses']['comp_sci']['assignment1']['grade'] == 100
	
@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem