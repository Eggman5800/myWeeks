import time
from typing import Any, List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: int, data: Any, hash: str, nonce: int):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce  # Add nonce attribute

    def __repr__(self):
        return (f"Block(index={self.index}, "
                f"previous_hash='{self.previous_hash}', "
                f"timestamp={self.timestamp}, "
                f"data='{self.data}', "
                f"hash='{self.hash}', "
                f"nonce={self.nonce})")

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the first block, called the Genesis Block."""
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", "0", 0)
        genesis_block.hash = self.calculate_hash(genesis_block)
        return genesis_block

    def get_latest_block(self) -> Block:
        """Returns the most recent block in the chain."""
        return self.chain[-1]

    def add_block(self, data: Any):
        """Creates a new block with given data and appends it to the blockchain."""
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = int(time.time())

        # Find a nonce that produces a hash with a certain condition
        nonce = 0
        hash_value = ''
        while True:
            hash_value = self.calculate_hash_for_new_block(new_index, latest_block.hash, new_timestamp, data, nonce)
            # Here, we are checking if the hash starts with '0000' (this is just an example condition)
            if hash_value.startswith('0000'):
                break
            nonce += 1

        new_block = Block(new_index, latest_block.hash, new_timestamp, data, hash_value, nonce)
        self.chain.append(new_block)

    def calculate_hash(self, block: Block) -> str:
        """Calculates hash for a given block."""
        block_data = f"{block.index}{block.previous_hash}{block.timestamp}{block.data}{block.nonce}"
        return self.sha1(block_data.encode())

    def calculate_hash_for_new_block(self, index: int, previous_hash: str, timestamp: int, data: Any, nonce: int) -> str:
        """Calculates hash for new block's data."""
        block_data = f"{index}{previous_hash}{timestamp}{data}{nonce}"
        return self.sha1(block_data.encode())

    def sha1(self, message: bytes) -> str:
        """Implements a basic SHA-1 hashing algorithm."""
        # Padding
        original_byte_len = len(message)
        original_bit_len = original_byte_len * 8
        message += b'\x80'  # Append a single '1' bit
        while (len(message) * 8) % 512 != 448:
            message += b'\x00'  # Pad with '0' bits

        message += original_bit_len.to_bytes(8, 'big')  # Append the original length

        # Initialize hash values
        h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]

        # Process each 512-bit chunk
        for i in range(0, len(message), 64):
            chunk = message[i:i + 64]
            w = [0] * 80

            # Break chunk into sixteen 32-bit big-endian words
            for j in range(16):
                w[j] = int.from_bytes(chunk[j * 4:j * 4 + 4], 'big')

            for j in range(16, 80):
                w[j] = self._left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)

            a, b, c, d, e = h

            for j in range(80):
                if j < 20:
                    f = (b & c) | (~b & d)
                    k = 0x5A827999
                elif j < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif j < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                else:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = (self._left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
                e = d
                d = c
                c = self._left_rotate(b, 30)
                b = a
                a = temp

            # Add the compressed chunk to the current hash value
            h = [(x + y) & 0xFFFFFFFF for x, y in zip(h, [a, b, c, d, e])]

        # Produce the final hash value (big-endian)
        return ''.join(x.to_bytes(4, 'big').hex() for x in h)

    def _left_rotate(self, value: int, amount: int) -> int:
        """Left rotates a value by the specified amount."""
        return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF

    def is_chain_valid(self) -> bool:
        """Validates the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correctly calculated
            if current_block.hash != self.calculate_hash(current_block):
                print("Invalid hash at block", i)
                return False

            # Check if the previous block's hash matches
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash at block", i)
                return False

        return True

# Example usage:
if __name__ == "__main__":
    blockchain = Blockchain()
    print("Genesis Block:", blockchain.get_latest_block())

    # Add new blocks with different types of data
    blockchain.add_block("First block data")
    blockchain.add_block({"transaction": "TX1001", "amount": 250})
    blockchain.add_block(["item1", "item2", "item3"])

    # Print the blockchain with nonce
    for block in blockchain.chain:
        print(block)

    # Check if blockchain is valid
    print("Is blockchain valid?", blockchain.is_chain_valid())
