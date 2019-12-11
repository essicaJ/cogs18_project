from my_functions import *

"""This function test if the class of major information works"""
def test_major_info():
    test_info = information.get('Psychology').name_func()
    assert isinstance(test_info, str)
    assert test_info == 'The major your are asking about is: Psychology B.S.'
    

"""This function test if the class of major courses works"""
def test_major_course():
    test_course = courses.get('Psychology Courses').lower_courses()
    assert isinstance(test_course, object)
    
    test = courses.get('Psychology Courses').lower_courses()
    assert test_course == test
