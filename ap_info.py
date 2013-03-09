# ap_info_py
# Includes general AP Credit class, and then dictionaries based on specific AP Credit policies of colleges

APEngineering = {'Art History': [(3, 4, 5), 5.3, 'lower_hss'], 'Biology': [(4, 5), 5.3, 'Biology 1A', 'Biology 1AL', 'Biology 1B'], 'Chemistry': [(3, 4, 5), 5.3, 'Chemistry 1A', 'Chemistry 1AL'], 'Chinese Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'Computer Science A': [(4, 5), 1.3], 'Economics (Macro)': [(3, 4, 5), 2.7, 'lower_hss'], 'Economics (Micro)': [(3, 4, 5), 2.7, 'lower_hss'], 'English Language': [(3), 5.3, 'entry_level_writing'], 'English Language': [(4, 5), 5.3, 'Reading and Composition "A"'], 'English Literature': [(3), 5.3, 'entry_level_writing'], 'English Literature': [(4, 5), 5.3, 'Reading and Composition "A"'], 'French Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'German Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'U.S. History': [(3, 4, 5), 5.3, 'lower_hss'], 'European History': [(3, 4, 5), 5.3, 'lower_hss'], 'World History': [(3, 4, 5), 5.3, 'lower_hss'], 'Human Geography': [(3, 4, 5), 5.3, 'lower_hss'], 'Italian Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'Japanese Language & Culture': [(3, 4, 5), 5.3, 'lower_hss'], 'Latin (Vergil)': [(3, 4, 5), 2.7], 'Latin Literature': [(3, 4, 5), 2.7], 'Calculus AB': [(3), 2.7, 'Math 1A'], 'Calculus AB': [(4, 5), 5.3, 'Math 1A', 'Math 1B'], 'Calculus BC': [(3), 5.3, 'Math 1A'], 'Calculus BC': [(4, 5), 5.3, 'Math 1A', 'Math 1B'], 'Music Theory': [(3, 4, 5), 5.3, 'lower_hss'], 'Physics B': [(3, 4, 5), 5.3], 'Physics C: Electricity & Magnetism': [(3, 4, 5), 5.3], 'Physics C: Mechanics': [(5), 2.7, 'Physics 7A'], 'Art History': [(3, 4, 5), 5.3, 'lower_hss'], 'Political Science (U.S.)': [(3, 4, 5), 2.7, 'lower_hss'], 'Political Science (Comparative)': [(3, 4, 5), 2.7, 'lower_hss'], 'Psychology': [(3, 4, 5), 2.7, 'lower_hss'], 'Spanish Language': [(3, 4, 5), 5.3, 'lower_hss'], 'Spanish Literature': [(3, 4, 5), 5.3, 'lower_hss'], 'Statistics': [(3, 4, 5), 2.7]} 
APLS = {}
class APCreditMain:
    """Returns credit received based on each AP Exam."""
    ap_credit = {}
    def get_credit(self, student_dict, college):
        """Returns dictionary with keys of APs taken, values in list of format [credit, Skippable Courses]"""
        for key in Student.apdict:
            ap_credit[key] = [] #For each AP taken creates key, value pair in ap_credit
        #ap_credit will be filled differently depending on value of college
        if college.lower() == 'engineering':
            for key in Student.apdict:
                for i in range(len(APEngineering[key][0])):
                    if Student.apdict[key] == APEngineering[key][0][i]:
                        ap_credit[key] = APEngineering[key][1:]
        elif college.lower() == 'l&s' or college.lower() == 'letters and sciences':
            for key in Student.apdict:
                for i in range(len(APLS[key][0])):
                    if Student.apdict[key] == APLS[key][0][i]:
                        ap_credit[key] = APLS[key][1:]
        #IMPLEMENT REST OF COLLEGE CASES HERE
        return ap_credit
