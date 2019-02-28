#!/usr/bin/python3
from slide import Slide
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit(84)

slideShow = []
means_nb_tags = 0
nb_image = 0
with open(sys.argv[1]) as f:
    for line in f:
        array = line.split(' ')
        if len(array) > 1:
            slideShow.append(Slide(array[0], array[2:], array[1]))
            means_nb_tags += int(array[1])
        else:
            nb_image = int(array[0])
print  (int(means_nb_tags / nb_image))
