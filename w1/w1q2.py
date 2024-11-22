#w1q2
##using arithmetic ops
print("--------------Arithmetic ops---------------")
a = int(input("enter first no A:"))
b = int(input("enter second no B:"))

a = a + b
b = a - b
a = a - b

print("value of A after swapping",a)
print("value of B after swapping",b)

##using bitwise ops
print("\n--------------Bitwise ops---------------")
c = int(input("enter first no C:"))
d = int(input("enter second no D:"))

c = c ^ d
d = c ^ d
c = c ^ d

print("value of C after swapping",c)
print("value of D after swapping",d)