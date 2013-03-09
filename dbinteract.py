from course_info import Course
import sqlite3

def add_courses(courses):
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    for course in courses:
        if course.abbrv and course.num and course.title:
            params = [course.abbrv, course.num, course.title, course.units,
                      course.pnp, course.technical]
            c.execute("insert into courses (abbrv, num, title, units, pnp, technical)"
                      + " values (?, ?, ?, ?, ?, ?)", params)
    conn.commit()
    conn.close()

def add_prereqs(name, prereqs):
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    courseid = find_id_coursecode(name)
    for prereq in prereqs:
        prereqid = find_id_coursecode(prereq)
        if prereqid and courseid:
            c.execute("insert into prereqs values (?, ?)", [courseid, prereqid])
    conn.commit()
    conn.close()

def get_course(name):
    return get_course_by_id(find_id_coursecode(name))

def get_course_by_id(courseid):
    if courseid:
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()
        c.execute("select * from courses where id = ?", [courseid])
        row = c.fetchall()[0]
        prereqs = get_prereqs_by_id(courseid)
        course = Course(row[1], str(row[2]), row[3], row[4], row[5], row[6], prereqs)
    else:
        course = None
    return course

def get_prereqs(name):
    return get_prereqs_by_id(find_id_coursecode(name))

def get_prereqs_by_id(courseid):
    result = set()
    if courseid:
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()
        c.execute("select prereqid from prereqs where courseid = ?", [courseid])
        rows = c.fetchall()
        for row in rows:
            prereq = get_course_by_id(row[0])
            result.add(str(prereq.abbrv) + ' ' + str(prereq.num))
    conn.close()
    return sorted(list(result))

def find_id_coursecode(name):
    num = name.split()[-1]
    abbrv = name[:(len(name)-len(num)-1)]
    return find_id(abbrv, num)

def find_id(abbrv, num):
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    c.execute("select id from courses where abbrv=:abbrv and num=:num",
                      {'abbrv': abbrv, 'num': num})
    result = c.fetchone()
    if result:
        result = result[0]
    conn.commit()
    conn.close()
    return result
