#w4q3
d1 = {"hello":1, 45:2}
d2 = {45:4, "!!":2}
d3 = {"this":5, 16:"world"}
d4 = {"message":7, 16:8}

newDict = {**d1, **d2, **d3, **d4}

print(newDict)