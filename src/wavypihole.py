#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)
epd = epd2in13_V2.EPD() # get the display
epd.init(epd.FULL_UPDATE)
logging.info("=============")
logging.info("Starting")


white = 1
black = 0

def printToDisplay(string):
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)

    image1 = Image.new('1', (epd.height, epd.width), 255)  # You only need to initialize this container once
    bmp = Image.open(os.path.join(picdir, 'logo.bmp'))
    image1.paste(bmp, (2,2))    # Paste the bmp over the container
    draw = ImageDraw.Draw(image1)  # Initialize ImageDraw over the container
    draw.text((25, 30), string, font = font, fill = white) # 
    epd.display(epd.getbuffer(image1))


msg = "Hello World and such!"
printToDisplay(msg)
