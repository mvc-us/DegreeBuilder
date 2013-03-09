#student_info.py
# this file contains the list of majors, the Major class, 
# as well as the implementation of an individual student
# please document as follows:
	# @params
	# what function does
	# @return#student_info.py
# this file contains the list of majors, the Major class, 
# as well as the implementation of an individual student
# please document as follows:
	# @params
	# what function does
	# @return
from algorithm import *
from ap_info import *
from course_info import *

class Major:
    #majors is a dictionary of majors with determined courses (dictionaries of key major + option, value list of required courses)
    #Later will be made into database of degree templates
    majors = {'eecsoption4': eecsoption4, 'eecsoption5': eecsoption5}
    def __init__(self):
        return


class Student(Major):
	"""Creates a profile for a student and his/her school schedule in order to graduate."""
	school_schedule = {} #Initial blank dictionary of graduation plan, including semesters taken
	def __init__(self, currentyear, gradyear, major, emphasis, college, apdict, taken_courses = {}, wanted_courses = []):
		"""Creates student profile and fills in the courses the student has taken so far.
		currentyear = current year of student #1.0 = Fall of First Year, 2.5 = Spring of Second Year
		gradyear = expected graduation year of student #Front end asks for Yr + Sem of graduation. 2016.5 = Spring 2016
		major = major of student #Drop down menu Front End. EECS = Electrical Engineering & Computer Science. Major object
        college = college of student #engineering, l&s, etc.
        emphasis = emphasis in major #For EECS, Option I-V as String
		apdict = dictionary with AP as key, score as value of APs student has taken #{'Calculus AB': 5, 'Calculus BC': 5, 'World History': 5}
		taken_courses = dictionary of courses student has already taken in a list corresponding to values of year they've been taken. #{1.0: ['MATH 53', 'EECS 61A', 'PHYSICS 7A', 'ANTHRO R5B']
		wanted_courses = list of courses student wants to take #['Music 26AC', 'Math 170']
		"""
		self.currentyear = currentyear
		self.gradyear = gradyear
        self.major = Major.majors[major + emphasis] #Example: For EECS Option V, self.major = eecsoption5
        self.emphasis = emphasis
        self.college = college
		self.aps_taken = apdict
        self.taken_courses = taken_courses
        self.wanted_courses = wanted_courses
		#populates school_schedule with courses already taken
		"""CODE HERE"""
		#Creates keys for each school sem in school_schedule
		#Example: currentyear = 1.5, gradyear = 2016.5 -> school_schedule = {1.0: [], 1.5: [], 2.0: [], 2.5: [], 3.0: [], 3.5: [], 4.0: [], 4.5: []}
		#Note: gradyear - currentyear - (4 - currentyear) = Current Calendar year 
		#Put taken_courses in school_schedule
		#Example: taken_courses = {1.0: ['Math 53', 'EECS 61A', 'Physics 7A', 'Anthro R5B']} -> school_schedule = {1.0: ['MATH 53', 'EECS 61A', 'PHYSICS 7A', 'ANTHRO R5B'], 1.5: [], 2.0: [], 2.5: [], 3.0: [], 3.5: [], 4.0: [], 4.5: []}
	def generate_schedule(self, algorithm, major = self.major):
        self.major = major #Reassigns student's major for algorithm purposes. i.e. first test using option4, then option5
        #if testing for new major, be sure to change back!
		"""Takes in and applies algorithm based on student's major to school_schedule."""
		student.school_schedule = algorithm(self) #Algorithm returns ideal graduation plan
		return student.school_schedule
        

#Manual degree templates, will be replaced by database
eecsoption4 = {'1.0': ['MATH 1A', 'SCIENCE', 'EECS 61A', 'HUMANITIES'], '1.5': ['MATH 1B', 'PHYSICS 7A', 'EECS 61B', 'HUMANITIES'], '2.0': ['MATH 53', 'PHYSICS 7B', 'EECS 61C', 'HUMANITIES'], '2.5': ['MATH 54', 'EECS 20N', 'EECS 70', 'HUMANITIES'], '3.0': ['PHYSICS 7C', 'EECS 40', 'EECS 162', 'TECHNICAL ELECTIVE'], '3.5': ['EECS 164', 'EECS 170', 'ELECTIVES', 'EECS 195'], '4.0': ['EECS 169', 'ENGINEERING', 'ELECTIVE', 'HUMANITIES'], '4.5': ['EECS 150', 'ENGINEERING', 'HUMANITIES', 'ELECTIVE']}
eecsoption5 = {'1.0': ['MATH 1A', 'SCIENCE', 'EECS 61A', 'HUMANITIES'], '1.5': ['MATH 1B', 'PHYSICS 7A', 'EECS 61B', 'HUMANITIES'], '2.0': ['MATH 53', 'PHYSICS 7B', 'EECS 20N', 'HUMANITIES'], '2.5': ['MATH 54', 'PHYSICS 7C', 'EECS 70', 'HUMANITIES'], '3.0': ['EECS 40', 'EECS 105', 'EECS 61C', 'TECHNICAL ELECTIVE'], '3.5': ['EECS 120', 'EECS 140', 'EECS 150', 'HUMANITIES'], '4.0': ['EECS 117', 'EECS 130', 'EECS 162', 'HUMANITIES'], '4.5': ['EECS 143', 'EECS 152', 'HUMANITIES', 'EECS 195']}





class Major:
	def __init__(self):
		return


class Student(Major):
	"""Creates a profile for a student and his/her school schedule in order to graduate."""
	school_schedule = {} #Initial blank dictionary of graduation plan, including semesters taken
	def __init__(self, currentyear, gradyear, major, emphasis, apdict, taken_courses = {}, wanted_courses = []):
		"""Creates student profile and fills in the courses the student has taken so far.
		currentyear = current year of student #1.0 = Fall of First Year, 2.5 = Spring of Second Year
		gradyear = expected graduation year of student #Front end asks for Yr + Sem of graduation. 2016.5 = Spring 2016
		major = major of student #Drop down menu Front End. EECS = Electrical Engineering & Computer Science
        	emphasis = emphasis in major #For EECS, Option I-V as String
		apdict = dictionary with AP as key, score as value of APs student has taken #{'Calculus AB': 5, 'Calculus BC': 5, 'World History': 5}
		taken_courses = dictionary of courses student has already taken in a list corresponding to values of year they've been taken. #{1.0: ['Math 53', 'CS 61A', 'Physics 7A', 'Anthro R5B']
		wanted_courses = list of courses student wants to take #['Music 26AC', 'Math 170']
		"""
		self.currentyear = currentyear
		self.gradyear = gradyear
		self.major = major
        	self.emphasis = emphasis
		self.aps_taken = apdict
		#populates school_schedule with courses already taken
		"""CODE HERE"""
		#Creates keys for each school sem in school_schedule
		#Example: currentyear = 1.5, gradyear = 2016.5 -> school_schedule = {1.0: [], 1.5: [], 2.0: [], 2.5: [], 3.0: [], 3.5: [], 4.0: [], 4.5: []}
		#Note: gradyear - currentyear - (4 - currentyear) = Current Calendar year 
		#Put taken_courses in school_schedule
		#Example: taken_courses = {1.0: ['Math 53', 'CS 61A', 'Physics 7A', 'Anthro R5B']} -> school_schedule = {1.0: ['Math 53', 'CS 61A', 'Physics 7A', 'Anthro R5B'], 1.5: [], 2.0: [], 2.5: [], 3.0: [], 3.5: [], 4.0: [], 4.5: []}
	def generate_schedule(self, algorithm, Major.major):
		"""Takes in and applies algorithm based on student's major to school_schedule."""
		student.school_schedule = algorithm(self) #Algorithm returns ideal graduation plan
		return student.school_schedule
        

majors = []
