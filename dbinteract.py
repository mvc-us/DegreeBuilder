import sqlite3

def add_courses(courses):
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    for course in courses:
        params = [course.abbrv, course.num, course.title, course.units,
                  course.pnp, course.technical]
        print params
        c.execute("insert into courses (abbrv, num, title, units, pnp, technical)"
                  + " values (?, ?, ?, ?, ?, ?)", params)
    conn.commit()
    conn.close()

def find_id_coursecode(name):
    num = name.split()[-1]
    abbrv = name[:(len(name)-len(num)-1)]
    return find_id(abbrv, num)

def find_id(abbrv, num):
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    count = c.execute("select id from courses where abbrv=:abbrv and num=:num",
                      {'abbrv': abbrv, 'num': num})
    if count > 0:
        result = c.fetchone()[0]
        conn.commit()
        conn.close()
        return result
    else:
        conn.commit()
        conn.close()
        return None
