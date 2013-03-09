# ap_info_py
# Includes general AP Credit class, and then dictionaries based on specific AP Credit policies of colleges

from course_info import *
from student_info import *
from algorithm import *
APEngineering = {'Art History': [(3, 4, 5), 5.3, 'lower_hss'], 'Biology': [(4, 5), 5.3, 'BIOLOGY 1A', 'BIOLOGY 1AL', 'BIOLOGY 1B'], 'Chemistry': [(3, 4, 5), 5.3, 'CHEM 1A', 'CHEM 1AL'], 'Chinese Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'Computer Science A': [(4, 5), 1.3], 'Economics (Macro)': [(3, 4, 5), 2.7, 'lower_hss'], 'Economics (Micro)': [(3, 4, 5), 2.7, 'lower_hss'], 'English Language': [(3), 5.3, 'entry_level_writing'], 'English Language': [(4, 5), 5.3, 'Reading and Composition "A"'], 'English Literature': [(3), 5.3, 'entry_level_writing'], 'English Literature': [(4, 5), 5.3, 'Reading and Composition "A"'], 'French Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'German Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'U.S. History': [(3, 4, 5), 5.3, 'lower_hss'], 'European History': [(3, 4, 5), 5.3, 'lower_hss'], 'World History': [(3, 4, 5), 5.3, 'lower_hss'], 'Human Geography': [(3, 4, 5), 5.3, 'lower_hss'], 'Italian Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'Japanese Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'Latin (Vergil)': [(3, 4, 5), 2.7], 'Latin Literature': [(3, 4, 5), 2.7], 'Calculus AB': [(3), 2.7, 'MATH 1A'], 'Calculus AB': [(4, 5), 5.3, 'MATH 1A', 'MATH 1B'], 'Calculus BC': [(3), 5.3, 'MATH 1A'], 'Calculus BC': [(4, 5), 5.3, 'MATH 1A', 'MATH 1B'], 'Music Theory': [(3, 4, 5), 5.3, 'lower_hss'], 'Physics B': [(3, 4, 5), 5.3], 'Physics C: Electricity & Magnetism': [(3, 4, 5), 5.3], 'Physics C: Mechanics': [(5), 2.7, 'PHYSICS 7A'], 'Art History': [(3, 4, 5), 5.3, 'lower_hss'], 'Political Science (U.S.)': [(3, 4, 5), 2.7, 'lower_hss'], 'Political Science (Comparative)': [(3, 4, 5), 2.7, 'lower_hss'], 'Psychology': [(3, 4, 5), 2.7, 'lower_hss'], 'Spanish Language': [(3, 4, 5), 5.3, 'lower_hss'], 'Spanish Literature': [(3, 4, 5), 5.3, 'lower_hss'], 'Statistics': [(3, 4, 5), 2.7]} 
APLS = {}
class APCreditMain:
    """Returns credit received based on each AP Exam."""
    def get_credit(self, student):
        """Returns dictionary with keys of APs taken, values in list of format [credit, Skippable Courses]"""
        student_dict = student.aps_taken
        ap_credit = {}
        for key in student:
            ap_credit[key] = [] #For each AP taken creates key, value pair in ap_credit
        #ap_credit will be filled differently depending on value of college
        if college.lower() == 'engineering':
            for key in student_dict:
                for i in range(len(APEngineering[key][0])):
                    if student_dict[key] == APEngineering[key][0][i]:
                        ap_credit[key] = APEngineering[key][1:]
        elif college.lower() == 'l&s' or college.lower() == 'letters and sciences':
            for key in student_dict:
                for i in range(len(APLS[key][0])):
                    if student_dict[key] == APLS[key][0][i]:
                        ap_credit[key] = APLS[key][1:]
        #IMPLEMENT REST OF COLLEGE CASES HERE
        return ap_credit

    def get_skipped(self, student):
        """Returns list of skipped classes."""
        student_dict = student.aps_taken
        skipped_classes = []
        #ap_credit will be filled differently depending on value of college
        if student.college.lower() == 'engineering':
            for key in student_dict:
                for i in range(len(APEngineering[key][0])):
                    if student_dict[key] == APEngineering[key][0][i]:
                        skipped_classes.extend(APEngineering[key][2:])
        elif student.college.lower() == 'l&s' or college.lower() == 'letters and sciences':
            for key in student_dict:
                for i in range(len(APLS[key][0])):
                    if student_dict[key] == APLS[key][0][i]:
                        skipped_classes.extend(APLS[key][2:])
        #IMPLEMENT REST OF COLLEGE CASES HERE
        return skipped_classes
