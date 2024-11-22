#w2q1f
import math

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
    
x = int(input("Enter the first side:"))
y = int(input("Enter the second side:\n"))
z = int(input("Enter the third side:\n"))

area = area_of_triangle(x, y, z)

type_of_triangle = triangle_type(x, y, z)

print("The area of the triangle is:",area)
print("The triangle is:" ,type_of_triangle)
