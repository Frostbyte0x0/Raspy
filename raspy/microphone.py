import asyncio
import logging


async def microphone_loop(queue: asyncio.Queue):
    try:
        while True:
            info = queue.get_nowait()
            if info != "":
                print("Listening!")
    except:
        logging.error(f"Task 'microphone' had an error")
