import asyncio
import logging


async def manager_loop(queue: asyncio.Queue):
    try:
        while True:
            info = queue.get_nowait()
            if info != "":
                print("Managing!")
    except:
        logging.error(f"Task 'manager' had an error")
