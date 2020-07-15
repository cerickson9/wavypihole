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

try:
    response = urllib2.urlopen('http://192.168.1.53/admin/api.php')

    json_string = response.read()
    parsed_json = json.loads(json_string)
    logging.debug(parsed_json)
    logging.debug(pprint(vars(your_object)))

    adsblocked = parsed_json[0]['ads_blocked_today']
#   ratioblocked = parsed_json['ads_percentage_today']
    f.close()
except:
    queries = '?'
    adsblocked = '?'
    ratio = '?'
    ratioblocked = '?'

logging.debug(adsblocked)
def printToDisplay():
    font = ImageFont.truetype(os.path.join(fontdir, 'FredokaOne-Regular.otf'), 20)
    smaller_font = ImageFont.truetype(os.path.join(fontdir, 'FredokaOne-Regular.otf'), 15)

    image1 = Image.new('1', (epd.height, epd.width), 255)  # You only need to initialize this container once
    bmp = Image.open(os.path.join(picdir, 'logo.bmp'))
    image1.paste(bmp, (2,2))    # Paste the bmp over the container
    draw = ImageDraw.Draw(image1)  # Initialize ImageDraw over the container

    draw.text((25, 20), str(adsblocked), font = font, fill = black) 
    draw.text((25, 50), "font example", font = font, fill = black) 
    draw.text((25, 100), str(d.month) + str(d.day) + "/" + "/" + str(d.year) + " ", font = smaller_font, fill = black)
    # draw.text((25, 50), str("%.1f" % round(ratioblocked,2)) + "%", font = font, fill = black) 
    epd.display(epd.getbuffer(image1))

printToDisplay()
