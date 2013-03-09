from flask import Flask, request, session, redirect, url_for, abort, g, render_template, flash
from ap_info import APEngineering

app = Flask(__name__)
app.config.from_object(__name__)

DATABASE = '/db/database.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

@app.route('/')
def index_page():
    return render_template('index.html', exams=sorted(exam_list()))

@app.route('/plan', methods=['POST'])
def plan_page():
    """The planning function. We perform data processing here."""
    args = request.form
    print args
    params = {}
    params['current'] = parse_semester(args['current'])
    params['grad'] = parse_semester(args['grad'])
    params['completed'] = int(args['completed'])
    params['major'] = str(args['major'])
    params['option'] = parse_option(args['option'])
    params['scores'] = exam_scores(args)
    print params
    return render_template('plan.html', params=params)

def parse_semester(semester):
    semester = semester.split()
    season = str(semester[0])
    year = int(semester[1])
    return (season, year)

def parse_option(option):
    optionmap = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
    return optionmap[option.split()[0]]

def exam_list():
    return APEngineering.keys()

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
