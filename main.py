from PIL import Image

name = "monkey.jpeg"
img = Image.open('src/input/' + name, 'r')
out = Image.new('RGB', img.size)


#get array full of color values for each pixel
inPixVal = list(img.getdata())
newPixVal = []

for color in inPixVal:
    col = (color[1], color[2], color[0])
    newPixVal.append(col)

#write new image
num = 0
for y in range(img.size[1]):
    for x in range(img.size[0]):
        out.putpixel((x,y), newPixVal[num])
        num+=1

out.show()

