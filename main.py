from PIL import Image

name = "ep.jpeg"
img = Image.open('src/input/' + name, 'r')
outl = Image.new('RGB', img.size)
outr = Image.new('RGB', img.size)



#get array full of color values for each pixel
inPixVal = list(img.getdata())
lVal = []
rVal = []

for color in inPixVal:
    col = (color[1], color[2], color[0])
    lVal.append(col)

for color in inPixVal:
    col = (color[2], color[0], color[1])
    rVal.append(col)

#write new image
num = 0
for y in range(img.size[1]):
    for x in range(img.size[0]):
        outl.putpixel((x,y), lVal[num])
        outr.putpixel((x,y), rVal[num])
        num+=1

outl.show()
outr.show()

