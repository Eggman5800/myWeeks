#w4q8
def sumVal(d):
    totals = sum(d.values())
    for key in d:
        d[key] = totals
    return d

dict = {'X':13, 'Y':26, 'Z':39}

newDict = sumVal(dict)
print(newDict)