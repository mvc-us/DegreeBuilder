from __future__ import with_statement
from contextlib import closing
from flask import Flask, request, session, redirect, url_for, abort, g, render_template, flash
from student_info import Student
from ap_info import APEngineering
import sqlite3

# temporary
DATABASE = '/db/database.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# from flask docs
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index_page():
    return render_template('index.html', exams=exam_list())

@app.route('/plan', methods=['POST'])
def plan_page():
    """The planning function. We perform data processing here."""
    args = request.form
    # print args
    params = {}
    params['current'] = parse_semester(args['current'])
    params['grad'] = parse_semester(args['grad'])
    params['completed'] = int(args['completed'])
    params['major'] = str(args['major'])
    params['option'] = parse_option(args['option'])
    params['courses'] = parse_courselist(args['courses'])
    params['scores'] = exam_scores(args)
    # print params
    semleft = semesters_left(params['current'], params['grad'])
    student = Student(semester_to_year(params['completed']), semleft,
                      params['major'], str(params['option']), apdict=params['scores'],
                      taken_courses=params['courses'])
    # schedule = student.generate_schedule()
    schedule = {'1.0': ['MATH 1A', 'SCIENCE', 'EECS 61A', 'HUMANITIES'], '1.5': ['MATH 1B', 'PHYSICS 7A', 'EECS 61B', 'HUMANITIES'], '2.0': ['MATH 53', 'PHYSICS 7B', 'EECS 61C', 'HUMANITIES'], '2.5': ['MATH 54', 'EECS 20N', 'EECS 70', 'HUMANITIES'], '3.0': ['PHYSICS 7C', 'EECS 40', 'EECS 162', 'TECHNICALELECTIVE'], '3.5': ['EECS 164', 'EECS 170', 'ELECTIVES', 'EECS 195'], '4.0': ['EECS 169', 'ENGINEERING', 'ELECTIVE', 'HUMANITIES'], '4.5': ['EECS 150', 'ENGINEERING', 'HUMANITIES', 'ELECTIVE']}
    orderedkeys = sorted(schedule.keys())
    return render_template('plan.html', schedule=schedule, keys=orderedkeys, n=len(orderedkeys))

def semester_to_year(completed):
    return 1.0 + (0.5 * completed)

def semesters_left(current, grad):
    seasoncurr = current[0]
    seasongrad = grad[0]
    yrcurr = current[1]
    yrgrad = grad[1]
    if seasoncurr == seasongrad:
        return 2*(yrgrad - yrcurr)
    else:
        return (2*(yrgrad - yrcurr)) - 1

def parse_semester(semester):
    semester = semester.split()
    season = str(semester[0])
    year = int(semester[1])
    return (season, year)

def parse_option(option):
    optionmap = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
    return optionmap[option.split()[0]]

def parse_courselist(strlist):
    return strlist.split(', ')

def exam_list():
    return sorted(APEngineering.keys())

def exams_taken(args):
    taken = []
    allexams = exam_list()
    for exam in allexams:
        if exam in args.keys():
            taken.append(exam)
    return taken

def exam_scores(args):
    exams = {}
    taken = exams_taken(args)
    for exam in taken:
        scorestr = exam + " score"
        exams[exam] = int(args[scorestr])
    return exams

if __name__ == '__main__':
    app.run()
