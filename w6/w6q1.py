import random
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def blum_blumShub(p, q, seed):
    n = p * q
    x = seed
    bits = []

    for _ in range(10):
        x = (x * x) % n
        bits.append(x % 2)

    return bits

def bitdec(bits):
    decimal = 0
    length = len(bits)
    for i in range(length):
        bit = bits[length - 1 - i]
        decimal += bit * (2 ** i)

    return decimal

p = 13  
q = 17 
seed = 65537

random_bits = blum_blumShub(p, q, seed)

print("Generated bits:", random_bits)

deci = bitdec(random_bits)
print("generated decimal: ",deci)