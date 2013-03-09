from course_info import Course
import urllib2, json

keys_to_api = {'abbrv':'departmentCode', 'num': 'courseNumber', 'title' :'courseTitle', 'units' :'upperUnits'}

app_id = "c47ea7e4"
app_key = "4da7dcb51c5f0887be363f0ebb0f85ff"

get_course_by_course_id = "https://apis-qa.berkeley.edu/cxf/asws/course?courseNumber={0}&_type=json&app_id={1}&app_key={2}"
get_course_term_info = "https://apis-qa.berkeley.edu/cxf/asws/classoffering?courseNumber={0}&departmentCode={1}&_type=json&app_id={2}&app_key={3}"

def get_all_courses():
        all_courses = []
        for i in range(1, 300):
                course_dict_list = get_courses(i)
                for course_dict in course_dict_list:
                        course = dict_to_course(course_dict)
                        all_courses.append(course)
        return all_courses

def get_courses(course_number):
        url = get_course_by_course_id.format(course_number, app_id, app_key)
        courses = get_json_from_url(url)
        course_dict_list = []
        if courses:
                courses = courses["CanonicalCourse"]
                for course in courses:
                        course_dict = {}
                        for key in keys_to_api:
                                try:
                                        value = course[keys_to_api[key]]
                                except KeyError:
                                        value = None
                                course_dict[key] = value
                        course_dict_list.append(course_dict)
        return course_dict_list

def get_json_from_url(url):
        try:
                req = urllib2.Request(url)
                opener = urllib2.build_opener()
                f = opener.open(req)
                return json.loads(f.read())
        except Exception:
                return None

def dict_to_course(course_dict):
        d = course_dict
        course = Course(d['abbrv'], d['num'], d['title'], d['units'])
        return course
