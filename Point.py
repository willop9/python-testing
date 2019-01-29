import math as m

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)
    def distFromOrgin(self):
        return m.sqrt((self.x ** 2) + (self.y ** 2))

    def distToPoint(self, p):
        if(self.x < p.x):
            lx = p.x - self.x
        else:
            lx = self.x - p.x
        if(self.y < p.y):
            ly = p.y - self.y
        else:
            ly = self.y - p.y
        return m.sqrt((lx ** 2) + (ly ** 2))

    def midpoint(self, p):
        mx = (self.x + p.x)/2
        my = (self.y + p.y)/2
        return Point(mx,my)
