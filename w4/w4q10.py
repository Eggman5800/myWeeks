#pangram
import string
def IsPangram(s):
    s = s.lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    set_alpha = set(alphabets)
    set_input = set(s)
    if (set_input == set_alpha):
        return True
    else:
        return False

str = "the Quick brown fox jumps over the lazy dog"
if IsPangram(str):
    print("It is a pangram.")
else:
    print("Not a pangram")