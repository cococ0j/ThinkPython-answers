import math
import copy

class Point(object):
    """Represents a point in 2-D space."""
    
class Rectangle():
    """
    Represents a rectangle
    useing its width, height and corner.
    corner is a point.
    """

def distance_between_two_point(p1,p2):
    x1 = p1.x - p2.x
    y1 = p1.y - p2.y
    distance = math.sqrt(x1**2 + y1**2)
    return distance

def print_point(p):
    print(p.x,p.y)
    
def print_rectangle(box):
    print(box.width,box.height,box.corner.x, box.corner.y)
    
def grow_rectangle(rectangle, dwidth, dheight):
    rectangle.width += dwidth
    rectangle.height += dheight

def move_rectangle(rect,dx,dy):
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return rect2

def main():
    box = Rectangle()
    box.width = 100
    box.height = 50
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0
    box2 = move_rectangle(box,2,3)
    print_rectangle(box2)
    
    
if __name__=='__main__':
    main()
