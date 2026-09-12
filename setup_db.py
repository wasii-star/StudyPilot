# Libraries
import sqlite3





DB_NAME = 'studypilot.db'
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
course_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
description TEXT,
learning_objective TEXT
)
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
task_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
deadline TEXT,
status TEXT,
dependencies TEXT,
course_id INTEGER,
FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
''')
conn.commit()
conn.close()