input_str = "Hello World"
res = ''

for char in input_str:
    xor_char = chr(ord(char) ^ 0)
    res += xor_char

print(res)
