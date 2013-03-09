#student_info.py
# this file contains the list of majors, the Major class, 
# as well as the implementation of an individual student
# please document as follows:
	# @params
	# what function does
	# @return



class Major:
	def __init__(self):
		return


class Student(Major):
	"""Creates a profile for a student and his/her school schedule in order to graduate."""
	school_schedule = {} #Initial blank dictionary of graduation plan, including semesters taken
	def __init__(self, currentyear, gradyear, major, aplist, taken_courses, wanted_courses = []):
		"""Creates student profile and fills in what the student has taken so far.
		currentyear = current year of student #1.0 = Fall of First Year, 2.5 = Spring of Second Year
		gradyear = expected graduation year of student #Front end asks for Yr + Sem of graduation. 2016.5 = Spring 2016
		major = major of student #Drop down menu Front End. EECS = Electrical Engineering & Computer Science
		aplist = list of String values of AP courses student has taken #['Calculus AB', 'Calculus BC', 'World History']
		taken_courses = dictionary of courses student has already taken in a list corresponding to values of year they've been taken. #{1.0: ['Math 53', 'CS 61A', 'Physics 7A', 'Anthro R5B']
		wanted_courses = list of courses student wants to take #['Music 26AC', 'Math 170']
		"""
		self.currentyear = currentyear
		self.gradyear = gradyear
		self.major = major
		self.aps_taken = aplist
		#populates school_schedule with courses already taken
		"""CODE HERE"""
		#Creates keys for each school sem in school_schedule
		#Example: currentyear = 1.5, gradyear = 2016.5 -> school_schedule = {1.0: [], 1.5: [], 2.0: [], 2.5: [], 3.0: [], 3.5: [], 4.0: [], 4.5: []}
		#Note: gradyear - currentyear - (4 - currentyear) = Current Calendar year 
		#Put taken_courses in school_schedule
		#Example: taken_courses = {1.0: ['Math 53', 'CS 61A', 'Physics 7A', 'Anthro R5B']}
		return


majors = []