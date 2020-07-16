#!/usr/bin/python
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'font')
if os.path.exists(libdir):
    sys.path.append(libdir)

import json
import requests
import urllib2
import urllib

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
    draw.text((25, 30), str('%.2f' % percentageblocked)  + '%', font = font, fill = black)
    draw.text((25, 50), str(totalqueries), font = font, fill = black) 
    draw.text((25, 100), str(d.month) + "/" + str(d.day)  + "/" + str(d.year) + " ", font = smaller_font, fill = black)
    epd.display(epd.getbuffer(image1))

json_string = requests.get('http://192.168.1.53/admin/api.php')
logging.debug(json_string)
parsed_json = json_string.json()
print json_string.headers['content-type']
print parsed_json
print type(parsed_json)


adsblocked = parsed_json['ads_blocked_today']
totalqueries = parsed_json['dns_queries_today']
percentageblocked = parsed_json['ads_percentage_today']
print adsblocked

printToDisplay()

