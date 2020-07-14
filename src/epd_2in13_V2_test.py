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
    background = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, 'logo.bmp'))
    background.paste(bmp, (2,2))    
    draw = Image.new('1', (epd.height, epd.width), 255)
    draw.text((25, 30), string, font = font, fill = white)

    epd.display(epd.getbuffer(background), epd.getbuffer(draw))
 

    # image1 = Image.new('1', (epd.height, epd.width), 255) 
    # text = Image.new('1', (epd.height, epd.width), 255)
    # logging.info('height: ')
    # logging.info(epd.height)
    # logging.info('width: ')
    # logging.info(epd.width)
    # bmp = Image.open(os.path.join(picdir, 'logo.bmp'))
    # image1.paste(bmp, (2,2))    
   
    # draw

    # draw.text((25, 30), string, font = font, fill = white)

    # epd.display_frame(epd.get_frame_buffer(image_black),epd.get_frame_buffer(image_red))

    epd.display(epd.getbuffer(background))

msg = "Hello Jeff!"
printToDisplay(msg)
