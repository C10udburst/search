import asyncio
from typing import List
from sys import stdout
import websockets

from classes import Result
from modules import get_threads
from utils.query import exception_pattern
from utils.results import result_json
from utils.thread import on_thread

from utils.config import config

PORT = int(config['websocket']['port'])


async def on_result(results: List[Result], websocket=None):
    send_threads = [websocket.send(result_json(result)) for result in results]
    await asyncio.gather(*send_threads)


async def on_recv(websocket, path):
    query = await websocket.recv()
    show_errors = bool(exception_pattern.search(" "+query+" "))
    threads = get_threads(query)
    threads = on_thread(threads, on_result, add_exceptions=show_errors,  websocket=websocket)
    await asyncio.gather(*threads, return_exceptions=True)


def run_websocket():
    print(f"Starting websocket on port {PORT}")
    stdout.flush()
    server = websockets.serve(on_recv, "127.0.0.1", PORT)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
