import pytest 
import System

def test_submit_assginment(grade_system):
	grade_system.login('hdjsr7', 'pass1234')
	
	grade_system.usr.submit_assignment('databases', 'assignment1', 'I did it', '3/3/20')
	grade_system.reload_data()
	
	assert grade_system.usr.users['hdjsr7']['courses']['databases']['assignment1']['submission'] == 'I did it'
	assert grade_system.usr.users['hdjsr7']['courses']['databases']['assignment1']['ontime'] == False

#I spent 20mins on this before i realized i forgot to add ['courses']

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem