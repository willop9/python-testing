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


print("hello World, this is my first python program")
name = "Will"
print("hello " + name)

o = Point()
p = Point(1,4)
q = Point(5,12)
distP = p.distFromOrgin()
distQ = q.distFromOrgin()
pString = str(p)
qString = str(q)
pLength = p.distToPoint(q)
qLength = q.distToPoint(p)
z = p.midpoint(q);
print(p.x, p.y, q.x, q.y)
print(distP, distQ)
print(pString,qString)
#Should be the same output
print(pLength, qLength)
#Finds midpoint and uses previous string
#method to correctly format the new point
print(str(z))
