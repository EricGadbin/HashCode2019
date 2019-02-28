#!/usr/bin/python3
from slide import Slide
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit(84)

# try :
pictures = []
i = 0
with open(sys.argv[1]) as f:
    for line in f:
        array = line.split(' ')
        # print (array)
        if len(array) > 1:
            pictures.append(Slide(array[0], array[2:], array[1], i))
            i += 1
# except:
#     sys.exit(84)
slide1 = None
slide2 = None
for slide in pictures:
    if (slide1 != None and slide.type == "V"):
        slide2 = slide
    if (slide1 == None and slide.type == "V"):
        slide1 = slide
    if (slide1 != None and slide2 != None):
        slide.ConcatV(slide1, slide2)
        pictures.pop(int(slide2.id[0]))
        slide1 = None
        slide2 = None

for slide in pictures:
    print (slide.id, slide.type, slide.nbTags, slide.tags)
