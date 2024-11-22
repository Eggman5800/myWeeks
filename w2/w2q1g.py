#w2q1g
def convert_case(char):
    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()
    else:
        return "Invalid input. Please enter an alphabetic character."

char = input("Enter a character: ")

if len(char) == 1:
    converted_char = convert_case(char)
    print("Converted character: ",converted_char)
else:
    print("Please enter a single character.")
