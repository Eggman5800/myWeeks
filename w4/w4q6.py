#w4q6
def sumVal(d):
    totals = sum(d.values())
    for key in d:
        d[key] = totals
    return d

dict = {'X':12, 'Y':24, 'Z':36}

newDict = sumVal(dict)
print(newDict)