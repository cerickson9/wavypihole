#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'font')
if os.path.exists(libdir):
    sys.path.append(libdir)

import json
import pickle
import urllib2
import logging
import datetime

from waveshare_epd import epd2in13_V2
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)
epd = epd2in13_V2.EPD() 
epd.init(epd.FULL_UPDATE)
logging.info("=============")
logging.info("Starting")

white = 1
black = 0
d = datetime.datetime.today()

def printToDisplay():
    font = ImageFont.truetype(os.path.join(fontdir, 'FredokaOne-Regular.otf'), 20)
    smaller_font = ImageFont.truetype(os.path.join(fontdir, 'FredokaOne-Regular.otf'), 10)

    image1 = Image.new('1', (epd.height, epd.width), 255)  # You only need to initialize this container once
    bmp = Image.open(os.path.join(picdir, 'logo.bmp'))
    image1.paste(bmp, (2,2))    # Paste the bmp over the container
    draw = ImageDraw.Draw(image1)  # Initialize ImageDraw over the container

    draw.text((25, 20), str(adsblocked), font = font, fill = black) 
    draw.text((25, 50), "example ", font = font, fill = black) 
    draw.text((25, 100), str(d.month) + "/" + str(d.day)  + "/" + str(d.year) + " ", font = smaller_font, fill = black)
    # draw.text((25, 50), str("%.1f" % round(ratioblocked,2)) + "%", font = font, fill = black) 
    epd.display(epd.getbuffer(image1))

try:
    response = urllib2.urlopen('http://192.168.1.53/admin/api.php')

    json_string = response.read()
    parsed_json = json.loads(json_string).decode('utf-8')
    logging.debug(parsed_json)
    decoded_json = json.dumps(parsed_json)
    json_final = pickle.loads(decoded_json)
    logging.debug(json_final)

    adsblocked = json_final['ads_blocked_today']
    ratioblocked = json_final['ads_percentage_today']
    f.close()
    printToDisplay()
except:
    queries = '?'
    adsblocked = '?'
    ratio = '?'
    ratioblocked = '?'
    printToDisplay()

logging.debug(adsblocked)
