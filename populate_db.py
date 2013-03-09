from getAllClasses import get_all_courses
from dbinteract import add_courses, add_prereqs

def init_prereqs():
    f = open('eecs_prereqs')
    lines = [line.strip().replace(';', '').replace('"', '') for line in f]
    f.close()
    for line in lines:
        prereq_struct = [course.strip() for course in line.split('->')]
        add_prereqs(prereq_struct[-1], prereq_struct[:len(prereq_struct)-1])

add_courses(get_all_courses)
init_prereqs()
