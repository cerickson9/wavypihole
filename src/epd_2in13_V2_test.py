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
    # image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    # draw = ImageDraw.Draw(image)

    # logging.info("=============")
    # logging.info("Printing")
    # bmpimage = Image.open(os.path.join(picdir, 'logo.bmp'))
    # font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 22)
    # draw = ImageDraw.Draw(bmpimage)
    # draw.text((25, 30), string, font = font, fill = white)
    # epd.display(epd.getbuffer(image))
    image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    logging.info('height: ' + epd.height + ' and width: ' + epd.width)
    bmp = Image.open(os.path.join(picdir, 'logo.bmp'))
    image1.paste(bmp, (2,2))    
    epd.display(epd.getbuffer(image1))

msg = "Hello Jeff!"
printToDisplay(msg)
