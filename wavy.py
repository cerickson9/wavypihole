import sys
sys.path.insert(1, "./lib") # Adds lib folder in this directory to sys
import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

epd = epd2in7b.EPD() # get the display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear(0xFF)      # clear the display

def printToDisplay(string):
  HBlackImage = Image.new('1', (epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), 255)
  HRedImage = Image.new('1', (epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), 255)

  draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)

  font = ImageFont.truetype('./fonts/Montserrat-Black', 30) # Create our font, passing in the font file and font size

  draw.text((25, 65), string, font = font, fill = 0)

  epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))

  printToDisplay("Hello, World!")

msg = "hiiiii"
printToDisplay(msg)
