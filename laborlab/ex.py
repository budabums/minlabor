import asyncio
from aiohttp import web

async def background_task():
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, some_sync_function)

app = web.Application()
app.on_startup.append(background_task)
