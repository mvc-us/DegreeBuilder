# course_info.py
# this script includes all Berkeley Courses and Departments
# also includes list of courses
# please document with javadoc format:
#       before function, list:
#               @params
#               what function does
#               @return

class Course:
        def __init__(self, abbrv, num, title = '', units = 0, pnp = 0, technical = 0, prereqs = []):
                self.abbrv = abbrv #String
                self.num = num #String
                self.title = title #String
                self.units = units #Float
                self.pnp = pnp #0 or 1
                self.technical = technical #0 or 1
                self.prereqs = prereqs #Compile all prereqs from database into list
