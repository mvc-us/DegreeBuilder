from __future__ import with_statement
from contextlib import closing
from flask import Flask, request, session, redirect, url_for, abort, g, render_template, flash
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
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# from flask docs
def init_db():
    with closing(connect_db()) as db:
        with register.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

# from flask docs
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

# from flask docs
@app.before_request
def before_request():
    g.db = connect_db()

# from flask docs
@app.teardown_request
def teardown_request(exception):
    g.db.close()

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

def store_course(course):
    

if __name__ == '__main__':
    app.run()
