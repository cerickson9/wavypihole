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
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
epd = epd2in13_V2.EPD() # get the display
epd.init(epd.FULL_UPDATE)
logging.info("=============")
logging.info("Starting")


white = 1
black = 0

def printToDisplay(string):
    image = Image.open(os.path.join(picdir, 'logo.png'))
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 22)
    draw = ImageDraw.Draw(image)

    while (True):
        draw.text((25, 30), string, font = font, fill = white)
        epd.display(epd.getbuffer(image))

msg = "Hello Jeff!"
printToDisplay(msg)
