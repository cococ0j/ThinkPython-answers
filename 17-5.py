
class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.x)+","+str(self.y)
    
    def __add__(self,other):
        if isinstance(other,Point):
            return self.add_point(other)
        else:
            return self.add_point_tuple(other)
        
    def add_point(self,other):
        t = Point()
        t.x = self.x + other.x
        t.y = self.y + other.y
        return t
    
    def add_point_tuple(self,t):
        temp = Point()
        temp.x = self.x + t[0]
        temp.y = self.y + t[1]
        return temp
    
    def __radd__(self,other):
        return self.__add__(other)
        
p = Point(1,2)
t = (3,4)
print(p+t)

