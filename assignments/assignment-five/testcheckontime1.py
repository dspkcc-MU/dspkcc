import pytest
import System

def test_check_ontime(grade_system):
	grade_system.login('akend3', '123454321')
	grade_system.usr.submit_assignment('comp_sci', 'assignment1', 'resubmit', '02/20/20')
	grade_system.reload_data()
	
	assert grade_system.usr.users ['akend3']['courses']['comp_sci']['assignment1']['ontime'] == 'false'
	
@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem