class Point(object):
    """Represents a point in 2-D space."""
    
class Rectangle():
    """
    Represents a rectangle
    useing its width, height and corner.
    corner is a point.
    """

def print_point(p):
    print(p.x,p.y)
    
def grow_rectangle(rectangle, dwidth, dheight):
    rectangle.width += dwidth
    rectangle.height += dheight

def move_rectangle(rect,dx,dy):
    rect.corner.x += dx
    rect.corner.y += dy

def main():
    box = Rectangle()
    box.width = 100
    box.height = 50
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0
    move_rectangle(box,2,3)
    print_point(box.corner)
    
if __name__=='__main__':
    main()
