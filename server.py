# Libraries
import os
from mcp.server.mcpserver import MCPServer

# MCP server
mcp = MCPServer('StudyPilot')




# Resources
@mcp.resource('notes://{note}')
def read_note(note):
    with open(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes', note), 'r'), 'r') as f:
        data = f.read()
        return data 

@mcp.resource('notes://list')
def list_notes():
    notes_list = os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes'))
    if notes_list == []:
        return 'No notes found'
    return '\n'.join(notes_list)

# Tools
# @mcp.tool()
# def search_notes(note:str):
#     if not note in notes:
#         return "note Not Found"
#     return note

mcp.run()



