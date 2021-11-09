# Finds the top 5% of unique colors, and only color shifts them

from PIL import Image
from operator import itemgetter
import math

name = "poster2.jpeg"
img = Image.open('src/input/' + name, 'r')
outl = Image.new('RGB', img.size)
outr = Image.new('RGB', img.size)

#get array full of color values for each pixel
inPixVal = list(img.getdata())
lVal = []
rVal = []
palette = {};

for color in inPixVal:
    if color in palette:
        palette[color] += 1
    else:
        palette[color] = 1

N = math.ceil(len(palette) / 5)
res = dict(sorted(palette.items(), key = itemgetter(1), reverse = True)[:N])
print(res)

for color in inPixVal:
    if isinstance(color, int):
        col = (255,255,255,0)
        lVal.append(col)
        rVal.append(col)
    elif color in res:
        col = (color[1], color[2], color[0])
        lVal.append(col)
        col = (color[2], color[0], color[1])
        rVal.append(col)
    else:
        lVal.append(color)
        rVal.append(color)
    

#write new image
num = 0
for y in range(img.size[1]):
    for x in range(img.size[0]):
        outl.putpixel((x,y), lVal[num])
        outr.putpixel((x,y), rVal[num])
        num+=1

outl.show()
outr.show()

