import pytest
import System

def test_student_adding_self (grade_system):
	username = 'akend3'
	password = '123454321'
	grade_system.login (username, password)
	
	grade_system.usr.add_student('akend3', 'software_engineering')
	grade_system.reload_data()
	
	assert 'software_engineering' in grade_system.usr.users["akend3"]['courses']
	
@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem
	
