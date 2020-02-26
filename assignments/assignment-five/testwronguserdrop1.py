import pytest
import System 

def test_student_trying_to_drop (grade_system):
	username = 'akend3'
	password = '123454321'
	grade_system.login (username, password)
	
	grade_system.usr.drop_student('akend3', 'databases')
	grade_system.reload_data()
	
	assert 'databases' not in grade_system.usr.users["akend3"]['courses']
	
@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem