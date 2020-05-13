'''Mohamed Mohamed May 13, 2020  ITEC 1150   Final Project'''

# Search Unsplash for a taco image (for example https://unsplash.com/photos/JiRSy0GfqPA)
# and save the image on your computer.
# The downloaded image is very large.
# Use pillow to resize the image to a smaller size,
# perhaps no more than 800px wide or tall (make sure you preserve the aspect ratio).
# Write the text "Random Taco Cookbook" on the image.
# Save the modified image to a new file.

from PIL import Image
from PIL import ImageFont, ImageDraw
import os

size = 640, 426

infile = "taco_original.jpg" # image file name

file, ext = os.path.splitext(infile) # spliting file name and file extension
im = Image.open(infile) # open file to read
im.thumbnail(size) # resize image to given size

draw = ImageDraw.Draw(im)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 22) # font and font size is given
draw.text((10, 25), "Random Taco Cookbook", font=font) # text is written

im.save(file + "_thumbnail.jpg", "JPEG") # saving file