#algorithm.py
# this document includes the algorithm for determining the ideal way to take courses

# @params: student(object)
# function computes ideal schedule
# @return: dict with the keys as semesters and values as lists of courses

from ap_info import *
from student_info import *
from course_info import *
FAILURE = -1

def algorithm(student):
	plan = dict(student.major.determined_courses)
	completed_courses = []
	needed_courses = []
	#im not positive about the following line of code, it should basically just add the courses that the person
	# has already taken coming from the taken_courses dict
	completed_courses.append([(item for item in student.taken_courses[key]) for key in student.taken_courses])
	completed_courses.append(apply_ap(student))
	for key in student.major.requirements:
		if len(key) == student.major.requirements[key]:

			for course in key:
				if course not in completed_courses:
					needed_courses.append(course)
			continue

		for course in key:
			if course in student.wanted_courses:
				needed_courses.append(wanted_courses)

	return course_map(plan, needed_courses)

# @return: dict of courses to/have take(n)
def course_map(student_dict, needed_courses, unit_cap = 16, technical_cap = 12):

	def add_later(course):
		needed_prereqs = list(course.prereqs)
		course_units = course.units

		pre_tech_total = 0
		if course.is_technical:
			pre_tech_total = course_units

		for key in student_dict:
			sem_total = course_units
			tech_total = pre_tech_total
			this_sem_prereq = False

			for course1 in student_dict[key]:
				sem_total += course1.units

				if course1.is_technical:
					tech_total += course1.units

				if course1 in needed_prereqs:
					needed_prereqs.remove(course1)
					this_sem_prereq = True

			if sem_total <= unit_cap and tech_total <= technical_cap and not this_sem_prereq:
				student_dict[key].append(course)
				return True

		return False


	def add_early(course):
		course_units = course.units

		pre_tech_total = 0
		if course.is_technical:
			pre_tech_total = course_units

		for key in student_dict:
			sem_total = course_units
			tech_total = pre_tech_total

			for course1 in student_dict[key]:
				sem_total += course1.units

				if course1.is_technical:
					tech_total += course1.units

				if sem_total > unit_cap or tech_total > technical_cap:
					break

			if sem_total <= unit_cap and tech_total <= technical_cap:
				student_dict[key].append(course)
				return True

		return False


	def scan_prereq(course):
		for prereq in course.prereqs:
			if prereq not in completed_courses:
				if prereq not in needed_courses:
					needed_courses.append(prereq)
				return False
		return True

	while len(needed_courses) != 0:
		for course in needed_courses:
			if len(course.prereqs) == 0:
				if add_early(course):
					needed_courses.remove(course)
				else:
					return {FAILURE: course}
			else:
				completed_courses = completed(student_dict)
				if scan_prereq(course):
					if add_later(course):
						needed_courses.remove(course)
					else:
						return {FAILURE: course}	


# @return: list of courses completed
def completed(student_dict):
	done = []
	for key in student_dict:
		done += student_dict[key]
	return done



#@return: list of APs applied
def apply_ap(student):
	used_APs = []
	def courses_replaced(ap_course_data):
		return ap_course_data[2:]

	for key in student.aps_taken:
		if courses_replaced(student.aps_taken[key]) == None: # for now, courses_replaced can be replaced with [2:]
			continue

		for course_tup in student.major.requirements:
			if courses_replaced(student.aps_taken[key]) in course_tup:
				used_APs.append(courses_replaced(student.aps_taken[key]))
				break
	return used_APs
