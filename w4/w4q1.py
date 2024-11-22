#w4q1
def countChar(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

str = "hello world!!"
count = countChar(str)
print(count)