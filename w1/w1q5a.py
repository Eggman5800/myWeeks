#w1q5a
def bigNumber(x,y,z):
    if(x>y) and (x>z):
        ##print(x,"is largest")
        return x
    elif y>z:
        ##print(y,"is largest")
        return y
    else:
        ##print(z,"is largest")
        return z
        
        
a = int(input("Enter the first no: "))
b = int(input("Enter the second no: "))
c = int(input("Enter the third no: "))

print("The largest no between",a,",",b,",",c,"is:",bigNumber(a, b, c))