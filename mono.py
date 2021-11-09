# Attempts to make a analagous color pallate by taking average of all colors, based on the most common color

from PIL import Image
from operator import itemgetter
import math

name = "ep.jpeg"
img = Image.open('src/input/' + name, 'r')
out = Image.new('RGB', img.size)

#get array full of color values for each pixel
inPixVal = list(img.getdata())
Val = []
palette = {};

# get unique colors
for color in inPixVal:
    if color in palette:
        palette[color] += 1
    else:
        palette[color] = 1

#get most common color
common = max(palette, key=palette.get)
print(common)

#Average all colors with most common
for color in inPixVal:
    r = math.floor((color[0] + common[0]) / 2)
    g = math.floor((color[1] + common[1]) / 2)
    b = math.floor((color[2] + common[2]) / 2)
    Val.append((r,g,b))
    

#write new image
num = 0
for y in range(img.size[1]):
    for x in range(img.size[0]):
        out.putpixel((x,y), Val[num])
        num+=1

out.show()

