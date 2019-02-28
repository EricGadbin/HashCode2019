
class Slide():
    def __init__(self, pictureType, tags, nbTags, picId):
        self.id = str(picId)
        self.type = pictureType
        self.nbTags = int(nbTags)
        self.tags = tags
        self.tags[self.nbTags - 1] = self.tags[self.nbTags - 1][: len(self.tags[self.nbTags - 1]) - 1]
        #print (self.id, self.type, self.nbTags, self.tags)

    def ConcatV(self, slide1, slide2):
        slide1.tags += slide2.tags
        slide1.tags = list(set(slide1.tags))
        slide1.id += " " + slide2.id
        slide1.type = "H"
        slide1.nbTags = len(slide1.tags)
