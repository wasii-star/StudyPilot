import asyncio
import os
from mcp import stdio_client, StdioServerParameters, ClientSession

server_params = StdioServerParameters(
    command="python3",
    args=[os.path.join(os.path.dirname(__file__),"server.py")],
)


async def main():
    print("1. Starting")

    async with stdio_client(server_params) as (read, write):
        print("2. Connected")

        async with ClientSession(read, write) as session:
            print("3. Session created")

            await session.initialize()
            print("4. Initialized")

            # resources = await session.list_resources()
            # print(resources)

            # templates = await session.list_resource_templates()
            # print(templates)

            # result = await session.read_resource("notes://python_basics.md")
            # print("5. Resource received")
            # print(result)
            
            # result = await session.call_tool("search_notes", {"query": "function"})
            # print(result)

            # result = await session.call_tool("add_course", {"name": "Python", "description": "Learn Python basics", "learning_objective": "Understand core syntax"})
            # print(result)

            # result = await session.read_resource("courses://list")
            # print(result)

            # result = await session.call_tool("add_task", {
            #     "name": "Finish loops exercise",
            #     "deadline": "2026-09-20",
            #     "status": "pending",
            #     "dependencies": "",
            #     "course_id": 1
            # })
            # print(result)

            # result = await session.read_resource("tasks://lists")
            # print(result)

            # result = await session.call_tool("convert_to_note", {"filepath": "/home/wasike/Downloads/module2.pdf"})
            # print(result)

            # result = await session.read_resource("notes://module2.md")
            # print(result)

            result = await session.get_prompt("prepare_study_session", {"course_name": "Python"})
            print(result)

asyncio.run(main())
