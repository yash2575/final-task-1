import sqlite3

def connectToDB():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todo
                      (todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       status INTEGER NOT NULL)''')
    # reset the auto-increment counter after clearing all records
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='todo'")
    conn.commit()
    conn.close()


def insertDB(title):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todo (title, status) VALUES (?, ?)", (title, 0))
    conn.commit()
    conn.close()

def viewData():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todo")
    rows = cursor.fetchall()
    return rows

def updateData(id):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	# cursor.execute('DELETE FROM todo')
	cursor.execute("UPDATE todo SET status = 1 WHERE todo_id=?", (id,))
	conn.commit()
	conn.close()

def deleteData(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todo WHERE todo_id=?", (id,))
    cursor.execute("SELECT todo_id FROM todo")
    rows = cursor.fetchall()
    for i, row in enumerate(rows, start=1):
        cursor.execute("UPDATE todo SET todo_id=? WHERE todo_id=?", (i, row[0]))
    conn.commit()
    conn.close()

def clearIds():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE todo SET todo_id=NULL")
    conn.commit()
    conn.close()


def clearAll():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todo")
    conn.commit()
    # reassign ids starting from 1
    cursor.execute("SELECT todo_id FROM todo")
    clearIds()
    # ids = [row[0] for row in cursor.fetchall()]
    # i = 0
    # for id in ids:
    #     cursor.execute("UPDATE todo SET todo_id=? WHERE todo_id=?", (i, id))
    #     i += 1
    conn.commit()
    conn.close()