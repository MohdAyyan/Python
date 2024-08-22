import math
def circle(radius):
    area = math.pi * (radius ** 2);
    circumference = 2 * math.pi * radius;
    return area,circumference;
a,c = circle(2);
print("Area : ",math.floor(a),"Circumference : ",math.floor(c))