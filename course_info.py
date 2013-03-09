#course_info.py
# this script includes all Berkeley Courses and Departments
# also includes list of courses
# please document with javadoc format:
# 	before function, list:
# 		@params
# 		what function does
# 		@return


class Course:
	def __init__(self, department_abbrv, course_num, course_title = '', units, p_np = False, is_technical = False, prereqs = []):
        self.department_abbrv = department_abbrv #String
        self.course_num = course_num #String
        self.course_title = course_title #String
        self.units = units #Float
        self.p_np = p_np #Boolean
        self.is_technical = is_technical #Boolean
        self.prereqs = prereqs #Compile all prereqs from database into list
