import asyncio
import logging
import sys

from raspy.speaker import speaker_loop
from raspy.screen import screen_loop

# noinspection PyArgumentList
logging.basicConfig(
    encoding='utf-8',
    level=10,
    handlers=[
        logging.FileHandler("raspy.log", mode="w"),
        logging.StreamHandler(sys.stdout)
    ],
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


async def main():
    queue = asyncio.Queue(maxsize=10)

    screen_task = asyncio.create_task(screen_loop(queue))
    speaker_task = asyncio.create_task(speaker_loop(queue))



if __name__ == "__main__":
    # Start the event loop and execute the main coroutine
    asyncio.run(main())