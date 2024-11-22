def CaesarEnc(str):
    shft = 3
    cipher = ''
    for char in str:
        if char.islower():
            cipher += chr((ord(char)+shft-97) % 26 + 97)
        elif char.isupper():
            cipher += chr((ord(char)+shft-65) % 26 + 65)
        else:
            cipher += char
    return cipher
def CaesarDec(str):
    shft = -3
    cipher = ''
    for char in str:
        if char.islower():
            cipher += chr((ord(char)+shft-97) % 26 + 97)
        elif char.isupper():
            cipher += chr((ord(char)+shft-65) % 26 + 65)
        else:
            cipher += char
    return cipher

coded = CaesarEnc("hello world")
print(coded)
decoded = CaesarDec("khoor zruog")
print(decoded)