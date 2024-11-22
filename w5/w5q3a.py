def messageBlocks(message): 
    binary = ''.join(format(ord(char), '08b') for char in message)
    padding_length = (64 - len(binary) % 64) % 64
    binary += '0' * padding_length
    blocks = [binary[i:i+64] for i in range(0, len(binary), 64)]
    return blocks

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

def initPerm(block):
    return ''.join(block[i-1] for i in IP)

# Example message
message = "The quick brown fox jumps over the lazy dog"

# Step 1: Divide into 64-bit blocks
blocks = messageBlocks(message)
print("Blocks before permutation:", blocks)

# Step 2: Apply Initial Permutation to each block
perm = [initPerm(block) for block in blocks]

# Output the permuted blocks
for i in range(len(perm)):
    print("Block", i+1, ":", perm[i])

