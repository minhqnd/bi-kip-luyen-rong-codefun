# đm công thức này chưa học nên phải google
a,b,c = map(int,input().split())
import math
def area_of_triangle(a, b, c):
    # calculate the semiperimeter
    s = (a + b + c) / 2
    # calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

print(area_of_triangle(a,b,c))
