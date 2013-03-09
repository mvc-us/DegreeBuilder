#course_info.py
# this script includes all Berkeley Courses and Departments
# also includes list of courses
# please document with javadoc format:
#         before function, list:
# 		@params
# 		what function does
# 		@return


class Course:
	def __init__(self, abbrv, num = 'SEE LIST', title = '', units, pnp = 0, technical = 0, prereqs = []):
		self.abbrv = abbrv #String
		self.num = num #String
		self.title = title #String
		self.units = units #Float
		self.pnp = pnp #0 or 1
		self.technical = technical #0 or 1 #decide in Course from database
		self.prereqs = prereqs #Compile all prereqs from database into list
        
#Needs to be instantiated for algorithm to work. But how to assign String to be Course object?
#Example: Algorithm appends 'HUMANITIES' as a required course. 'HUMANITIES' refernces what?
HUMANITIES = Course('HUMANITIES',units = 4.0)
SCIENCE = Course('SCIENCE', units = 4.0, is_technical = 1)
ELECTIVE = Course('ELECTIVE', units = 4.0)
ELECTIVES = Course('ELECTIVES', units = 4.0)
TECHNICAL ELECTIVE = Course('TECHNICAL ELECTIVE', units = 4.0, is_technical = 1)
