#!/usr/bin/python3
from slide import Slide
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit(84)

# try :
slideShow = []
with open(sys.argv[1]) as f:
    for line in f:
        array = line.split(' ')
        # print (array)
        if len(array) > 1:
            slideShow.append(Slide(array[0], array[2:], array[1]))
# except:
#     sys.exit(84)
