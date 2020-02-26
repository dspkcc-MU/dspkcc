import pytest
import System

def test_add_student (grade_system):
	username = 'goggins'
	password = 'augurrox'
	grade_system.login (username, password)
	
	grade_system.usr.add_student('akend3', 'software_engineering')
	grade_system.reload_data()
	
	assert 'software_engineering' in grade_system.usr.users["akend3"]['courses']
	
@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem
	
#I see this is the one where it fails because a line in the professors file is wrong self.users[self.name][‘courses’][course]