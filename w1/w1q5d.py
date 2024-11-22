#w1q5d
import math
def volcube(s):
    vol = math.pow(s, 3)
    return vol

def volcyl(r,h):
    vol = (math.pi * math.pow(r, 2) * h)
    return vol

def volbox(l,b,h):
    vol = l * b * h
    return vol

x = int(input("Select the shape by entering the shape no.:\n1.Cube\n2.Cylinder\n3.Box\nENTER HERE:"))

if (x == 1):
    print("You have selected CUBE\n")
    a = int(input("Enter the side of the cube: "))
    print("Volume of the cube is: ",volcube(a))
elif (x == 2):
    print("You have selected CYLINDER\n")
    rad = float(input("Enter the radius of the cylinder: "))
    hit = float(input("\nEnter the height of the cylinder: "))
    print("Volume of the cylinder is: ",volcyl(rad, hit))
elif (x == 3):
    print("You have selected BOX\n")
    l = int(input("Enter the length of the box: "))
    b = int(input("\nEnter the breadth of the box: "))
    h = int(input("\nEnter the height of the box: "))
    print("Volume of the box is: ",volbox(l, b, h))
else:
    print("Invalid selection, please try again!!!")
    