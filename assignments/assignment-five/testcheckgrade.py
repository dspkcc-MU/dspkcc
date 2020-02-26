import pytest
import System

def test_grade_check (grade_system):
	grade_system.login ('akend3', '123454321')
	#grade_system.usr.check_grades('comp_sci')
	
	assert  grade_system.usr.check_grades('comp_sci')[0] == ['assignment1', 'N/A']

#will have to check why grade was changed to N/A and not 100


@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem
