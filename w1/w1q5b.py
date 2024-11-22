#w1q5b
def fibonacci(n):
    a = 0
    b = 1
    if n<0:
        print("Invalid input!!")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

for i in range(0,4):
    print(fibonacci(i))
