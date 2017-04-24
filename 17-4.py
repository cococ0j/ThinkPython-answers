class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+","+str(self.y)
    def __add__(self,other):
        temp = Point()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp
    
p = Point(1,2)
t = Point(3,4)
print(p+t)

