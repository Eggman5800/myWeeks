#w4q2
def countWord(s):
    frequency = {}
    for word in s.lower().split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

str = "Hello World Hello from the world in the particle portal"
count = countWord(str)
print(count)