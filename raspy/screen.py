import asyncio
import logging

import digitalio
import board
from PIL import Image
# Import your specific display driver
from adafruit_st7789 import ST7789

# 1. Define Wiring Connections (Adjust these to match your hardware layout)
CS_PIN = board.CE0      # Chip Select pin
DC_PIN = board.D24      # Data/Command pin (often labeled DC or RS)
RESET_PIN = board.D25   # Reset pin (often labeled RST)
BACKLIGHT = board.D22   # Backlight control pin (optional)

# 2. Setup SPI Bus and Pins
spi = board.SPI()
tft_cs = digitalio.DigitalInOut(CS_PIN)
tft_dc = digitalio.DigitalInOut(DC_PIN)
tft_rst = digitalio.DigitalInOut(RESET_PIN)

# 3. Turn on Backlight (if applicable)
blk = digitalio.DigitalInOut(BACKLIGHT)
blk.direction = digitalio.Direction.OUTPUT
blk.value = True

# 4. Initialize Display Driver
# Change 'ST7789' to your chip configuration (e.g., ST7735R, ILI9341)
# Adjust the width and height to match your physical panel resolution
display = ST7789(
    spi,
    cs=tft_cs,
    dc=tft_dc,
    rst=tft_rst,
    width=240,
    height=320,
    rotation=180 # Options: 0, 90, 180, 270
)

# 5. Load and Process the Image File
image_path = "my_photo.jpg" # Change to your filename
image = Image.open(image_path)

# Automatically resize and crop image to fit the screen dimensions
image.thumbnail((display.width, display.height), Image.Resampling.LANCZOS)

# Create a blank background matching the display resolution
background = Image.new("RGB", (display.width, display.height), (0, 0, 0))

# Center the resized image onto the blank background
paste_x = (display.width - image.width) // 2
paste_y = (display.height - image.height) // 2
background.paste(image, (paste_x, paste_y))

# 6. Push the final image array out to the TFT Screen
display.image(background)
print(f"Successfully displaying {image_path}!")


async def screen_loop(queue: asyncio.Queue):
    try:
        while True:
            info = queue.get_nowait()
            if info != "":
                print("Showing!")
    except:
        logging.error(f"Task 'screen' had an error")
