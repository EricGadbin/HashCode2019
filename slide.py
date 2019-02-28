
class Slide():
    def __init__(self, pictureType, tags, nbTags, picId):
        self.id = picId
        self.type = pictureType
        self.nbTags = int(nbTags)
        self.tags = tags
        self.tags[self.nbTags - 1] = self.tags[self.nbTags - 1][: len(self.tags[self.nbTags - 1]) - 1]
        print (self.id, self.type, self.nbTags, self.tags)
