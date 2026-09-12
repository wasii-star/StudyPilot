# Libraries
import os
from mcp.server.mcpserver import MCPServer

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

mcp.run()



