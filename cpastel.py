# Finds the top 5% of unique colors, and adds white to them to make the whole image feel softer, hopefully without just making the entire thing whiter

from PIL import Image
import math
from operator import itemgetter

name = "poster2.jpeg"
img = Image.open('src/input/' + name, 'r')
out = Image.new('RGB', img.size)

#get array full of color values for each pixel
inPixVal = list(img.getdata())
val = []
palette = {}

for color in inPixVal:
    if color in palette:
        palette[color] += 1
    else:
        palette[color] = 1

print(f"palette size: {len(palette)}")
#get 5 largest values in dictionary
N = math.ceil(len(palette) / 5)
res = dict(sorted(palette.items(), key = itemgetter(1), reverse = True)[:N])
print(res)

for color in inPixVal:
    # find ratio to number, and then move it to a a range of 140-255
    # value = %white of original 255 * range of 115 nums possible + 140 starting value
    # doing them all makes it just look brighter. Going to try doing this, but keep dominant color where it is
    if color in res:
        r = math.ceil((color[0] / 255) * 115 + 140)
        g = math.ceil((color[1] / 255) * 115 + 140)
        b = math.ceil((color[2] / 255) * 115 + 140)
        col = (r,g,b)
        val.append(col)
    else:
        val.append(color)
    

#write new image
num = 0
for y in range(img.size[1]):
    for x in range(img.size[0]):
        out.putpixel((x,y), val[num])
        num+=1

out.show()

