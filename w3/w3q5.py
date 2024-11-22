#w3q5
def reverse_words(s):
    words = s.split()
    return ' '.join(reversed(words))

s = "My name is Michele"
reversed_words = reverse_words(s)
print("String with words in backward order:", reversed_words)
