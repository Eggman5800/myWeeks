import time
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, year: int, student_data: List[Dict[str, str]], difficulty: int = 2):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = int(time.time())
        self.year = year
        self.student_data = student_data  # List of dictionaries containing student details
        self.nonce = 0  # Nonce is initially set to 0
        self.difficulty = difficulty  # Number of leading zeros required in the hash
        self.hash = self.mine_block()

    def calculate_hash(self) -> str:
        """Calculates the SHA-1 hash of the block's contents."""
        block_content = f"{self.index}{self.previous_hash}{self.timestamp}{self.year}{self.student_data}{self.nonce}"
        return self.sha1(block_content.encode())

    def mine_block(self) -> str:
        """Performs proof-of-work by finding a hash that meets the difficulty level."""
        computed_hash = self.calculate_hash()
        # Continue to increment nonce until a hash with required leading zeros is found
        while not computed_hash.startswith('0' * self.difficulty):
            self.nonce += 1
            computed_hash = self.calculate_hash()
        return computed_hash

    @staticmethod
    def sha1(message: bytes) -> str:
        """SHA-1 hash function implementation."""
        # Padding
        original_byte_len = len(message)
        original_bit_len = original_byte_len * 8
        message += b'\x80'  # Append a single '1' bit
        while (len(message) * 8) % 512 != 448:
            message += b'\x00'  # Pad with '0' bits

        message += original_bit_len.to_bytes(8, 'big')  # Append the original length as a 64-bit big-endian integer

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
                w[j] = Block._left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)

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

                temp = (Block._left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
                e = d
                d = c
                c = Block._left_rotate(b, 30)
                b = a
                a = temp

            # Add the compressed chunk to the current hash value
            h = [(x + y) & 0xFFFFFFFF for x, y in zip(h, [a, b, c, d, e])]

        # Produce the final hash value (big-endian)
        return ''.join(x.to_bytes(4, 'big').hex() for x in h)

    @staticmethod
    def _left_rotate(value: int, amount: int) -> int:
        """Left rotates a 32-bit integer value by the specified amount."""
        return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF

    def __repr__(self):
        return f"Block(index={self.index}, year={self.year}, hash={self.hash}, previous_hash={self.previous_hash}, nonce={self.nonce}, student_data={self.student_data})"

class Blockchain:
    def __init__(self, difficulty: int = 2):
        self.difficulty = difficulty  # Set difficulty for mining
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the first block in the blockchain, with default genesis data."""
        return Block(0, "0", 0, [{"name": "Genesis Block", "student_id": "0", "department": "N/A"}], self.difficulty)

    def get_latest_block(self) -> Block:
        """Returns the latest block in the blockchain."""
        return self.chain[-1]

    def add_block(self, year: int, student_data: List[Dict[str, str]]):
        """Adds a new block for a specific year with a list of M.Sc. students' details."""
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, year, student_data, self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks if the blockchain's integrity is maintained."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                print(f"Hash mismatch at block {i}")
                return False
            if current_block.previous_hash != previous_block.hash:
                print(f"Previous hash mismatch at block {i}")
                return False
        return True

# Example usage:
if __name__ == "__main__":
    # Initialize blockchain with a difficulty level of 2
    student_blockchain = Blockchain(difficulty=2)
    
    # Add student details for a particular year
    student_blockchain.add_block(
        2023,
        [
            {"Name": "SAUD", "Student_id": "23CSMSA105", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "John", "Student_id": "23CSMSA112", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "AMIR", "Student_id": "23CSMSA122", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "AHMAD", "Student_id": "23CSMSA123", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "JUNAID", "Student_id": "23CSMSA125", "Department": "Computer Science", "Course": "M.Sc."},
        ]
    )

    student_blockchain.add_block(
        2024,
        [
            {"Name": "Mohdsaud", "Student_id": "24CSMSA108", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "saim", "Student_id": "24CSMSA111", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "mohsin", "Student_id": "24CSMSA112", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "suhail", "Student_id": "24CSMSA113", "Department": "Computer Science", "Course": "M.Sc."},
            {"Name": "Faiz", "Student_id": "24CSMSA114", "Department": "Computer Science", "Course": "M.Sc."},
        ]
    )

    # Print the blockchain
    for block in student_blockchain.chain:
        print(block)

    # Check if blockchain is valid
    print("Is blockchain valid?", student_blockchain.is_chain_valid())
