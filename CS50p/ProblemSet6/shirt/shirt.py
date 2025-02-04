from PIL import Image
import os
import sys
import PIL

if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")

ifile,iext = os.path.splitext(sys.argv[1])
ofile,oext = os.path.splitext(sys.argv[2])
if iext not in [".jpg",".jpeg", ".png"]:
    sys.exit("Invalid input")
if iext != oext:
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
b = Image.open(sys.argv[1])
size = shirt.size
a = PIL.ImageOps.fit(b,size)
a.paste(shirt, shirt)
a.save(sys.argv[2])
