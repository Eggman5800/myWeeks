#w3q2
def charfrequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s = "Hello, World!!"
frequency = charfrequency(s)
print("Character frequency is:", frequency)
