def generate_rsa_keys(bit_length=512):
    p = random_prime(2^bit_length)
    q = random_prime(2^bit_length)
    while p == q:
        q = random_prime(2^bit_length)
    
    
    n = p * q
    phi = (p - 1) * (q - 1)


    e = 65537 
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime")

    d = inverse_mod(e, phi)

    return (e, n), (d, n)  # (public key, private key)


def encrypt(message, public_key):
    e, n = public_key
    # Convert message to integer
    m = Integer(message)
    # Encryption: c = m^e mod n
    c = power_mod(m, e, n)
    return c



def decrypt(ciphertext, private_key):
    d, n = private_key
    # Decryption: m = c^d mod n
    m = power_mod(ciphertext, d, n)
    return m



public_key, private_key = generate_rsa_keys()



message = 42


ciphertext = encrypt(message, public_key)
print(f"Ciphertext: {ciphertext}")



decrypted_message = decrypt(ciphertext, private_key)
print(f"Decrypted Message: {decrypted_message}")