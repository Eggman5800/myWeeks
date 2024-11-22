import math

def calculate_target(bits: int) -> int:
    # Extract exponent and coefficient from bits
    exponent = bits >> 24
    coefficient = bits & 0xFFFFFF
    # Calculate target
    target = coefficient * (256 ** (exponent - 3))
    return target

def calculate_difficulty(target: int) -> float:
    # Max target for Bitcoin's genesis block
    max_target = 0xFFFF * (256 ** (0x1d - 3))
    # Calculate difficulty
    difficulty = max_target / target
    return difficulty

def leading_zeros_required(target: int) -> int:
    # SHA-256 hash is 256 bits, calculate leading zeros by difference
    target_bits = target.bit_length()
    leading_zeros = 256 - target_bits
    return leading_zeros

def probability_of_valid_hash(difficulty: float) -> float:
    # Probability of a random hash being valid (using inverse of difficulty)
    probability = 1 / difficulty
    return probability

# Given values
bits = 386414640
nonce = 1131420428

# Calculations
target = calculate_target(bits)
difficulty = calculate_difficulty(target)
leading_zeros = leading_zeros_required(target)
probability = probability_of_valid_hash(difficulty)

# Display results
print(f"a. Current Target: {target}")
print(f"b  Current Difficulty: {difficulty}")
print(f"c. Leading Zeros Required in SHA-256 Hash: {leading_zeros}")
print(f"d. Probability of a Valid Hash: {probability:.10e}")
