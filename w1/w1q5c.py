#w1q5c
def facto(f):
    if (f==0 or f==1):
        return 1
    else:
        return (f * facto(f-1))

##print(facto(4))
for i in range(1,11):
    print("\n",facto(i))