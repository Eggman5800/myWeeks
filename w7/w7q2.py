import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_prime(length):
    while True:
        p = random.getrandbits(length) | (1 << (length - 1)) | 1
        if is_prime(p):
            return p

def find_primitive_root(p):
    # Step 1: Calculate p-1
    p_minus_1 = p - 1
    factors = []

    # Step 2: Find prime factors of p-1
    for i in range(2, int(p_minus_1**0.5) + 1):
        while p_minus_1 % i == 0:
            if i not in factors:
                factors.append(i)
            p_minus_1 //= i
    if p_minus_1 > 1:
        factors.append(p_minus_1)

    # Step 3: Check for primitive roots
    for g in range(2, p):
        is_primitive = True
        for factor in factors:
            if pow(g, (p - 1) // factor, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return g
    return None

def diffie_hellman_key_exchange():
    # Step 1: Generate a large prime number p
    p = generate_prime(8)  # Generate a smaller prime for demonstration (8 bits)
    print(f"Prime p: {p}")

    # Step 2: Find a primitive root g modulo p
    g = find_primitive_root(p)
    print(f"Primitive root g: {g}")

    # Step 3: Generate private keys
    a = random.randint(1, p - 2)  # Alice's private key
    b = random.randint(1, p - 2)  # Bob's private key

    # Step 4: Compute public keys
    A = pow(g, a, p)  # Alice's public key
    B = pow(g, b, p)  # Bob's public key

    print(f"Alice's public key A: {A}")
    print(f"Bob's public key B: {B}")

    # Step 5: Compute shared secrets
    shared_secret_A = pow(B, a, p)  # Alice computes the shared secret
    shared_secret_B = pow(A, b, p)  # Bob computes the shared secret

    print(f"Alice's shared secret: {shared_secret_A}")
    print(f"Bob's shared secret: {shared_secret_B}")

    assert shared_secret_A == shared_secret_B, "Shared secrets do not match!"

# Run the Diffie-Hellman key exchange
diffie_hellman_key_exchange()
