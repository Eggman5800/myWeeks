#w2q1b
x = int(input("Enter the first:"))
y = int(input("Enter the second:\n"))
z = int(input("Enter the third:\n"))

if (x<=y) and (x<=z):
    print(x," is the smallest no.")

elif (y<=x) and (y<=z):
    print(y," is the smallest no.")

else:
    print(z," is the smallest no.")            