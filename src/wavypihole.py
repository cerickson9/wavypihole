#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'font')
if os.path.exists(libdir):
    sys.path.append(libdir)

import json, ast
import pickle
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
    draw.text((25, 50), "example ", font = font, fill = black) 
    draw.text((25, 100), str(d.month) + "/" + str(d.day)  + "/" + str(d.year) + " ", font = smaller_font, fill = black)
    # draw.text((25, 50), str("%.1f" % round(ratioblocked,2)) + "%", font = font, fill = black) 
    epd.display(epd.getbuffer(image1))

def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )

def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data
    
try:
    response = urllib2.urlopen('http://192.168.1.53/admin/api.php')

    json_string = response.read()
    
    unicode_json = json.loads(json_string)
    parsed_json = ast.literal_eval(json.dumps(unicode_json))
    logging.debug(parsed_json)
    logging.debug(type(parsed_json))
    adsblocked = parsed_json["ads_blocked_today"]
    ratioblocked = parsed_json["ads_percentage_today"]
    f.close()
    # printToDisplay()
except:
    queries = '?'
    adsblocked = '?'
    ratio = '?'
    ratioblocked = '?'
    # printToDisplay()

logging.debug(adsblocked)
