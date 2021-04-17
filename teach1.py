'''import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Line:
    def __init__(self, p0, p1):
        self.x = p1.getX() - p0.getX()  
        self.y = p1.getY() - p0.getY()
        self.len = math.sqrt(self.x * self.x + self.y * self.y)

    def getlen(self):
        return self.len
p0=Point(1,2)
p1=Point(2,3)
line=Line(p0,p1)
print(line.getlen())
'''
class Ticket:
    def __init__(self,weekend = False,child = False):
        self.a = 100
        if weekend:
            self.discount1 = 1.2
        else:
            self.discount1 = 1
            if child:
                self.discount2 = 0.5
            else:
                self.discount1 = 1

    def getadult(self,num):
        return self.a*num*self.discount1

    def getchild(self,num):
        return self.a*num*self.discount2
   
adult = Ticket(weekend=False,child=False)
child = Ticket(weekend=False,child=True)
print("2个成人+1个小孩平日票价为:%.2f" %(adult.getadult(2)+child.getchild(1)))