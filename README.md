# StudyPilot

A student productivity assistant built with MCP (Model Context Protocol).

## What it does

- Read and search markdown notes
- Convert PDFs/docs/excel files into notes automatically
- Track courses and tasks in a SQLite database
- A prompt that helps prep for a study session

## Setup

git clone <https://github.com/wasii-star/StudyPilot.git>
cd StudyPilot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Run

python3 server.py

Then connect with the MCP Inspector, or run client.py to test it directly.

## Structure

- server.py — the MCP server (resources, tools, prompt)
- client.py — a simple client for testing
- notes/ — markdown notes
- studypilot.db — SQLite database (courses, tasks)

## Database

courses: course_id, name, description, learning_objective
tasks: task_id, name, deadline, status, dependencies, course_id (links to courses)

## MCP concepts used

- Resources: notes://list, notes://{note}, courses://list, tasks://list
- Tools: search_notes, convert_to_note, add_course, add_task
- Prompt: prepare_study_session