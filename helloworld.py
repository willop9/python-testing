import math as m

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distFromOrgin(self):
        return m.sqrt((self.x ** 2) + (self.y ** 2))
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)


print("hello World, this is my first python program")
name = "Will"
print("hello " + name)

o = Point()
p = Point(1,4)
q = Point(4,9)
distP = p.distFromOrgin()
distQ = q.distFromOrgin()

print(p.x, p.y, q.x, q.y)
print(distP, distQ)
