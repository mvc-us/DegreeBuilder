#algorithm.py
# this document includes the algorithm for determining the ideal way to take courses

# @params: student(object)
# function computes ideal schedule
# @return: dict with the keys as semesters and values as lists of courses

from dbinteract import get_course
from ap_info import *
from student_info import *
from course_info import *
import random

HUMAN = ['ANTHRO 2AC', 'SLAVIC R5A', 'ANTHRO R5B', 'HISTORY 11', 'ASAMST 125', 'HISTORY 4', 'PSYCH 2', 'GWS 10', 'GWS 125', 'MUSIC 26AC', 'SOCIOL 3AC', 'PHILOS 25A', 'COG SCI 1', 'ECON 100A', 'UGBA 10', 'EA LANG C50', 'CLASSIC 28', 'LINGUIS 5', 'POL SCI C79']
SCIENCE = ['CHEM 4A', 'ASTRON 10', 'MCELLBI 61', 'EPS C20']
ELECTIVE = ['EECS 188', 'EECS 122', 'EECS 172', 'EECS 126']

FAILURE = -1

def algorithm(student):
	plan = dict(student.major.determined_courses)
	for i in range(1, student.num_semesters + 1):
		if i not in plan:
			plan[i] = []
	completed_courses = []
	needed_courses = []
	
	for item in student.taken_courses:
		completed_courses.append(item)

	ap = APCreditMain()
	completed_courses.extend(ap.get_skipped(student))

	req = completed(plan)
	for course in completed_courses:
		if course in req:
			map_del(plan, course)

	for key in student.major.requirements:
		if len(key) == student.major.requirements[key]:
			for course in key:
				if course not in completed_courses:
					needed_courses.append(course)
			
	if course in student.wanted_courses:
		needed_courses.append(wanted_courses)

	return course_map(plan, needed_courses, student, completed_courses)

# @return: dict of courses to/have take(n)
def course_map(student_dict, needed_courses, student, completed_courses, unit_cap = 16, technical_cap = 12):

	def add_later(course):
		needed_prereqs = list(course.prereqs)
		course_units = course.units

		pre_tech_total = 0
		if course.technical:
			pre_tech_total = course_units

		for key in student_dict:
			sem_total = course_units
			tech_total = pre_tech_total
			this_sem_prereq = False

			for course1 in student_dict[key]:
				course1 = get_course(course1)
				if not course1:
					sem_total += 0
				else:
					sem_total += course1.units

					if course1.technical:
						tech_total += course1.units

					if course1 in needed_prereqs:
						needed_prereqs.remove(course1.toString())
						this_sem_prereq = True

			if sem_total <= unit_cap and tech_total <= technical_cap and not this_sem_prereq:
				student_dict[key].append(course.toString())
				return True

		return False


	def add_early(course):
		course_units = course.units

		pre_tech_total = 0
		if course.technical:
			pre_tech_total = course_units

		for key in student_dict:
			sem_total = course_units
			tech_total = pre_tech_total

			for course1 in student_dict[key]:
				course1 = get_course(course1)
				if not course1:
					sem_total += 0
				else:
					sem_total += course1.units

					if course1.technical:
						tech_total += course1.units

					if sem_total > unit_cap or tech_total > technical_cap:
						break

			if sem_total <= unit_cap and tech_total <= technical_cap:
				student_dict[key].append(course.toString())
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
			course = get_course(course)
			if not course: continue
			if len(course.prereqs) == 0:
				for i in range(3):
					map_del(student_dict, course.toString())
				if add_early(course):
					needed_courses.remove(course.toString())
					completed_courses.append(course.toString())
				else:
					return student_dict #return {FAILURE: course}
			else:
				completed_courses = completed(student_dict)
				if scan_prereq(course):
					map_del(student_dict, course.toString())
					if add_later(course):
						needed_courses.remove(course.toString())
						completed_courses.append(course.toString())
					else:
						return student_dict #{FAILURE: course}

	for key in student.major.requirements:
		need = student.major.requirements[key]
		for item in key:
			if item in completed_courses:
				need -= 1
				if need <= 0:
					break

		while need > 0:
			test_course = random.choice(key)
			print test_course
			if test_course not in completed_courses:
				completed_courses.append(test_course)
				add_later(get_course(test_course))
				need -= 1

	return student_dict



# @return: list of courses completed
def completed(student_dict):
	humanities_rep(student_dict)
	science_rep(student_dict)
	done = []
	for key in student_dict:
		done += student_dict[key]
	return done

#@return void
def map_del(student_dict, course):
	for key in student_dict:
		for item in student_dict[key]:
			if course == item:
				student_dict[key].remove(course)
				return None
				
def humanities_rep(student_dict):
	for i in range(6):
		for key in student_dict:
			student_dict[key] = [x.replace("HUMANITIES", random.choice(HUMAN)) for x in student_dict[key]]		

def science_rep(student_dict):
	for i in range(6):
		for key in student_dict:
			student_dict[key] = [x.replace("SCIENCE", random.choice(SCIENCE)) for x in student_dict[key]]

def elective_rep(student_dict):
	for key in student_dict:
		for item in student_dict[key]:
			if item.find('ELECTIVE') != -1:
				student_dict[key].remove(item)
				student_dict[key].append(random.choice(ELECTIVE))

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
