# Libraries
import os
from mcp.server.mcpserver import MCPServer
import sqlite3
#from markitdown import MarkItDown


DB_NAME = 'studypilot.db'


# MCP server
mcp = MCPServer('StudyPilot')




# Resources
@mcp.resource('notes://list')
def list_notes():
    '''Lists all available notes.'''
    notes_list = os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes'))
    if notes_list == []:
        return 'No notes found'
    return '\n'.join(notes_list)


@mcp.resource('notes://{note}')
def read_note(note):
    '''Reads a specific note.'''
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes', note), 'r') as f:
        data = f.read()
        return data 

@mcp.resource('courses://list')
def list_courses() -> str:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    rows = cursor.fetchall()
    courses_list = []
    for row in rows:
        course_info = f"{row[0]}: {row[1]}"
        courses_list.append(course_info)
    conn.close()    
    return '\n'.join(courses_list)    

@mcp.resource('tasks://lists')
def list_tasks() -> str:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT tasks.name, tasks.deadline, courses.name
    FROM tasks
    JOIN courses ON tasks.course_id = courses.course_id;
    ''')
    rows = cursor.fetchall()
    tasks_list = []
    for row in rows:
        task_info = f"{row[0]}: {row[1]}: {row[2]}"
        tasks_list.append(task_info)
    conn.close()    
    return '\n'.join(tasks_list)     




# Tools
@mcp.tool()
def search_notes(query:str):
    """Search all notes for a keyword and return matching filenames."""
    notes_list = list_notes()
    notes_list = notes_list.splitlines()
    matches = []
    for note in notes_list:
        seen_note = read_note(note)
        if query.lower() in seen_note.lower():
            matches.append(note)

    return matches

@mcp.tool()
def add_course(name, description, learning_objective):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO courses(name,description,learning_objective) VALUES (?,?,?)',(name,description,learning_objective))
    conn.commit()
    conn.close()
    return 'Course added successfully.'

    
@mcp.tool()
def add_task(name, deadline, status, dependencies, course_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks(name, deadline, status, dependencies, course_id) VALUES (?,?,?,?,?)',(name, deadline, status, dependencies, course_id))
    conn.commit()
    conn.close()
    return 'Task added successfully.'


mcp.run()






 