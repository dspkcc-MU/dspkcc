import pytest
import System 

def test_wrong_user_creating_assignment (grade_system):
	username = 'akend3'
	password = '123454321'
	grade_system.login (username, password)
	
	grade_system.usr.create_assignment ('homework 5', '02/25/20', 'software_engineering')
	grade_system.reload_data()
	
	assert 'homework 5' in grade_system.usr.all_courses ['software_engineering']['assignments']

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem