#w3q4
def first_last_chars(s):
    if len(s) < 2:
        return s
    return s[:2] + s[-2:]

s = "Hello, World!"
result = first_last_chars(s)
print("String with first 2 and last 2 chars:", result)
