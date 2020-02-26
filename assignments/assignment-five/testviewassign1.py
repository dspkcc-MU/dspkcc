import pytest
import System

def test_view(grade_system):
	grade_system.login('yted91', 'imoutofpasswordnames')
	#grade_system.usr.view_assignment('cloud_computing')
	
	assert grade_system.usr.view_assignments('cloud_computing')[0] == ['assignment1', '1/7/20'] 
	assert grade_system.usr.view_assignments('cloud_computing')[1] == ['assignment2', '2/7/20']

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem