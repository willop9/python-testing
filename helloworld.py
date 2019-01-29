from Point import Point
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
