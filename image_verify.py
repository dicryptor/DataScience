from PIL import Image

im = Image.open('401.jpg')
Image.load
print(im.format, "%dx%d" % im.size, im.mode)
