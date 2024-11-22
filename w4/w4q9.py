##write a python script to concatenate 3 dict in 1
d1 = {"hello":1, 45:2}
d2 = {45:4, "!!":2}
d3 = {"this":5, 16:"world"}

newDict = {**d1, **d2, **d3}

print(newDict)