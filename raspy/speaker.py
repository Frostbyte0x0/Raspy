import asyncio
import logging


async def speaker_loop(queue: asyncio.Queue):
    try:
        while True:
            info = queue.get_nowait()
            if info != "":
                print("Speaking!")
    except:
        logging.error(f"Task 'speaker' had an error")
