import time
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, semester: str, student_grades: List[Dict[str, str]]):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = int(time.time())
        self.semester = semester  # E.g., "Semester 1", "Semester 2"
        self.student_grades = student_grades  # List of dictionaries with each student's grades
        self.nonce = 0  # Initialize nonce
        self.hash = self.calculate_hash_with_nonce()

    def calculate_hash_with_nonce(self) -> str:
        """Calculates a valid SHA-1 hash with a nonce that satisfies a specific condition (e.g., starting with '0000')."""
        while True:
            block_content = f"{self.index}{self.previous_hash}{self.timestamp}{self.semester}{self.student_grades}{self.nonce}"
            hash_value = self.sha1(block_content.encode())
            if hash_value.startswith("0000"):  # Condition for a valid hash
                return hash_value
            self.nonce += 1

    @staticmethod
    def sha1(message: bytes) -> str:
        """Implements the SHA-1 hash function."""
        original_byte_len = len(message)
        original_bit_len = original_byte_len * 8
        message += b'\x80'
        while (len(message) * 8) % 512 != 448:
            message += b'\x00'
        message += original_bit_len.to_bytes(8, 'big')

        h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]

        for i in range(0, len(message), 64):
            chunk = message[i:i + 64]
            w = [0] * 80

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

            h = [(x + y) & 0xFFFFFFFF for x, y in zip(h, [a, b, c, d, e])]

        return ''.join(x.to_bytes(4, 'big').hex() for x in h)

    @staticmethod
    def _left_rotate(value: int, amount: int) -> int:
        """Left rotates a 32-bit integer value by the specified amount."""
        return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF

    def __repr__(self):
        return (f"Block(index={self.index}, semester={self.semester}, "
                f"previous_hash={self.previous_hash}, nonce={self.nonce}, hash={self.hash}, "
                f"student_grades={self.student_grades})")

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the first block in the blockchain with default genesis data."""
        return Block(0, "0", "Genesis Semester", [{"name": "Genesis Block", "student_id": "0", "grades": {}}])

    def get_latest_block(self) -> Block:
        """Returns the latest block in the blockchain."""
        return self.chain[-1]

    def add_block(self, semester: str, student_grades: List[Dict[str, str]]):
        """Adds a new block with students' grades for a specific semester."""
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, semester, student_grades)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks the blockchain's integrity."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash_with_nonce():
                print(f"Hash mismatch at block {i}")
                return False
            if current_block.previous_hash != previous_block.hash:
                print(f"Previous hash mismatch at block {i}")
                return False
        return True

# Example usage:
if __name__ == "__main__":
    # Initialize blockchain
    grade_blockchain = Blockchain()
    
    # Add student grades for Semester 1
    grade_blockchain.add_block(
        "Semester 1",
        [
            {"Name": "SARIM", "Student_id": "23CSMSA101", "Grades": {"Digital Forensics": "A", "Blockchain Technology": "B", "Cyber Security in IoT": "A+"}},
            {"Name": "RASHID", "Student_id": "23CSMSA102", "Grades": {"Digital Forensics": "O", "Blockchain Technology": "A", "Cyber Security in IoT": "B+"}},
            {"Name": "SUHAIL", "Student_id": "23CSMSA103", "Grades": {"Digital Forensics": "A+", "Blockchain Technology": "C", "Cyber Security in IoT": "B"}},
        ]
    )

    # Add student grades for Semester 2
    grade_blockchain.add_block(
        "Semester 2",
        [
            {"Name": "UMAIR", "Student_id": "23CSMSA101", "Grades": {"Network Forensics": "A", "Cyber Crime and Laws": "A+", "Security System Administrator": "B"}},
            {"Name": "KASHIF", "Student_id": "23CSMSA102", "Grades": {"Network Forensics": "B+", "Cyber Crime and Laws": "A", "Security System Administrator": "A+"}},
            {"Name": "ARIF", "Student_id": "23CSMSA103", "Grades": {"Network Forensics": "B", "Cyber Crime and Laws": "A", "Security System Administrator": "C"}},
        ]
    )

    # Print the blockchain
    for block in grade_blockchain.chain:
        print(block)

    # Check if blockchain is valid
    print("Is blockchain valid?", grade_blockchain.is_chain_valid())
