#student_info.py
# this file contains the list of majors, the Major class, 
# as well as the implementation of an individual student
# please document as follows:
# @params
# what function does
# @return
from algorithm import algorithm
from ap_info import *
from course_info import *

#Manual degree templates, will be replaced by database
eecs4 = {'1.0': ['MATH 1A', 'SCIENCE', 'EECS 61A', 'HUMANITIES'], '1.5': ['MATH 1B', 'PHYSICS 7A', 'EECS 61B', 'HUMANITIES'], '2.0': ['MATH 53', 'PHYSICS 7B', 'EECS 61C', 'HUMANITIES'], '2.5': ['MATH 54', 'EECS 20N', 'EECS 70', 'HUMANITIES'], '3.0': ['PHYSICS 7C', 'EECS 40', 'EECS 162', 'TECHNICALELECTIVE'], '3.5': ['EECS 164', 'EECS 170', 'ELECTIVES', 'EECS 195'], '4.0': ['EECS 169', 'ENGINEERING', 'ELECTIVE', 'HUMANITIES'], '4.5': ['EECS 150', 'ENGINEERING', 'HUMANITIES', 'ELECTIVE']}
eecs5 = {'1.0': ['MATH 1A', 'SCIENCE', 'EECS 61A', 'HUMANITIES'], '1.5': ['MATH 1B', 'PHYSICS 7A', 'EECS 61B', 'HUMANITIES'], '2.0': ['MATH 53', 'PHYSICS 7B', 'EECS 20N', 'HUMANITIES'], '2.5': ['MATH 54', 'PHYSICS 7C', 'EECS 70', 'HUMANITIES'], '3.0': ['EECS 40', 'EECS 105', 'EECS 61C', 'TECHNICALELECTIVE'], '3.5': ['EECS 120', 'EECS 140', 'EECS 150', 'HUMANITIES'], '4.0': ['EECS 117', 'EECS 130', 'EECS 162', 'HUMANITIES'], '4.5': ['EECS 143', 'EECS 152', 'HUMANITIES', 'EECS 195']}

class Major:
    #majors is a dictionary of majors with determined courses (dictionaries of key major + option, value list of required courses)
    #Later will be made into database of degree templates
    majors = {'eecs4': eecs4, 'eecs5': eecs5}

     #@params: dict of major requirements - (tuple of courses to choose from): int(# needed from these)
     # dict of determined courses - by default, what classes student will take in a given semester for the major
    def __init__(self, req_list_dict, determined_courses_dict):
        self.requirements = req_list_dict
        self.determined_courses = determined_courses_dict


class Student(Major):
    """Creates a profile for a student and his/her school schedule in order to graduate."""
    def __init__(self, currentyear, gradyear, major, emphasis, college = 'Engineering', apdict = {}, taken_courses = {}, wanted_courses = []):
        """Creates student profile and fills in the courses the student has taken so far.
        currentyear = current year of student #1.0 = Fall of First Year, 2.5 = Spring of Second Year
        gradyear = expected graduation year of student #Front end asks for Yr + Sem of graduation.
        major = major of student #Drop down menu Front End. EECS = Electrical Engineering & Computer Science. Major object
        college = college of student #engineering, l&s, etc.
        emphasis = emphasis in major #For EECS, Option I-V as String
        apdict = dictionary with AP as key, score as value of APs student has taken #{'Calculus AB': 5, 'Calculus BC': 5, 'World History': 5}
        taken_courses = dictionary of courses student has already taken in a list corresponding to values of year they've been taken. #{1.0: ['MATH 53', 'EECS 61A', 'PHYSICS 7A', 'ANTHRO R5B']
        wanted_courses = list of courses student wants to take #['Music 26AC', 'Math 170']
        """
        self.currentyear = currentyear
        self.gradyear = gradyear # ignore for now
        self.major = Major.majors[major.lower() + emphasis] #Example: For EECS Option V, self.major = eecsoption5
        self.emphasis = emphasis
        self.college = college
        self.aps_taken = apdict
        self.taken_courses = taken_courses
        self.wanted_courses = wanted_courses
        self.school_schedule = {} #Initial blank dictionary of graduation plan, including semesters taken
		#populates school_schedule with courses already taken
		#Creates keys for each school sem in school_schedule
		#Example: currentyear = 1.5, gradyear = 2016.5 -> school_schedule = {1.0: [], 1.5: [], 2.0: [], 2.5: [], 3.0: [], 3.5: [], 4.0: [], 4.5: []}
		#Note: gradyear - currentyear - (4 - currentyear) = Current Calendar year 
		#Put taken_courses in school_schedule
		#Example: taken_courses = {1.0: ['Math 53', 'EECS 61A', 'Physics 7A', 'Anthro R5B']} -> school_schedule = {1.0: ['MATH 53', 'EECS 61A', 'PHYSICS 7A', 'ANTHRO R5B'], 1.5: [], 2.0: [], 2.5: [], 3.0: [], 3.5: [], 4.0: [], 4.5: []}
    def generate_schedule(self, algo=algorithm):
        #Reassigns student's major for algorithm purposes. i.e. first test using option4, then option5
        #if testing for new major, be sure to change back!
        """Takes in and applies algorithm based on student's major to school_schedule."""
        self.school_schedule = algo(self) #Algorithm returns ideal graduation plan
        return self.school_schedule
