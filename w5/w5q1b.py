def SubsEnc(str,shft):
    cipher = ''
    for char in str:
        if char.islower():
            cipher += chr((ord(char)+shft-97) % 26 + 97)
        elif char.isupper():
            cipher += chr((ord(char)+shft-65) % 26 + 65)
        else:
            cipher += char
    return cipher

def SubsDec(str,shft):
    cipher = ''
    for char in str:
        if char.islower():
            cipher += chr((ord(char)+shft-97) % 26 + 97)
        elif char.isupper():
            cipher += chr((ord(char)+shft-65) % 26 + 65)
        else:
            cipher += char
    return cipher

message = "Change camp"
coded = SubsEnc(message,10)
print(coded)