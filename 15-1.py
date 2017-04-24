import math

class Point(object):
    """Represents a point in 2-D space."""

def distance_between_two_point(p1,p2):
    x1 = p1.x - p2.x
    y1 = p1.y - p2.y
    distance = math.sqrt(x1**2 + y1**2)
    return distance

def main():
    point1 = Point()
    point1.x = 1
    point1.y = 2
    point2 = Point()
    point2.x = 1
    point2.y = 3
    distance = distance_between_two_point(point1,point2)
    print(distance)
    
if __name__=='__main__':
    main()
