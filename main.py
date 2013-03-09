'''
main.py
this file depends on course_info.py , student_info.py
the algorithm and communication with the frontend should be done here
'''

from ap_info import *
from student_info import *
from course_info import *
from algorithm import *
from app.py import *

def make_demo(student):
    return generate_schedule(algorithm)
