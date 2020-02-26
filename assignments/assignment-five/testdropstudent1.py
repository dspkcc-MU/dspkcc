import pytest
import System 

def test_drop_student (grade_system):
	username = 'goggins'
	password = 'augurrox'
	grade_system.login (username, password)
	
	grade_system.usr.drop_student('akend3', 'databases')
	grade_system.reload_data()
	
	assert 'databases' not in grade_system.usr.users["akend3"]['courses']
	
@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem