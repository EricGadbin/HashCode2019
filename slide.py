
class Slide():
    def __init__(self, pictureType, tags, nbSlide):
        self.type = pictureType
        self.nbSlide = int(nbSlide)
        self.tags = tags
        self.tags[self.nbSlide - 1] = self.tags[self.nbSlide - 1][: len(self.tags[self.nbSlide - 1]) - 1]
