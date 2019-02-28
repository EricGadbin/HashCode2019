#!/usr/bin/python3
from slide import Slide
import random
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit(84)

pictures = []
slideShow = []
means_nb_tags = 0
nb_image = 0
moyenne = 0
with open(sys.argv[1]) as f:
    for line in f:
        array = line.split(' ')
        if len(array) > 1:
            pictures.append(Slide(array[0], array[2:], array[1], nb_image))
            means_nb_tags += int(array[1])
            nb_image += 1

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

def common_elements(list1, list2):
    return len([element for element in list1 if element in list2])

def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return len(li_dif)

def calcul_score(slide1, slide2):
    dif = diff (slide1.tags, slide2.tags)
    same1 = common_elements (slide1.tags, slide2.tags)
    same2 = common_elements (slide2.tags, slide1.tags)
    # print (same1, same2, dif)
    return (min (min (dif, same1), same2))

moyenne  = int(means_nb_tags / nb_image)
moyenne = round(moyenne)



j = 0
while (j < len (pictures)):
    if (pictures[j].type == "V"):
        del pictures[j]
    j += 1


random.shuffle(pictures)
slideShow.append(pictures[0])
del pictures[0]
score = 0
index = 0
tmp = 0
i = 0
while (len(pictures) != 0):
    i = 0
    index = 0
    for i in range (len(pictures)):
        tmp = calcul_score(slideShow[-1], pictures[i])
        if (tmp > score):
            index = i
            score = tmp
        i += 1
    slideShow.append(pictures[index])
    del pictures[index]

print (len(slideShow))
for element in slideShow:
    print (element.id)