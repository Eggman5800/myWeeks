import hashlib
import time

# Initialize blockchain with a genesis block
blockchain = []

def calculate_hash(block):
    content = str(block['index']) + str(block['timestamp']) + str(block['data']) + str(block['previous_hash']) + str(block['nonce'])
    return hashlib.sha256(content.encode()).hexdigest()


def mine_block(block, difficulty):
    target = '0' * difficulty
    while not block['hash'].startswith(target):
        block['nonce'] += 1
        block['hash'] = calculate_hash(block)
    print("Block mined with hash:", block['hash'])
    return block


def create_block(index, previous_hash, data, difficulty=4):
    nonce = 0
    timestamp = time.time()
    block = {
        'index': index,
        'timestamp': timestamp,
        'data': data,
        'previous_hash': previous_hash,
        'nonce': nonce,
        'difficulty': difficulty,
        'hash': ''
    }
    block['hash'] = calculate_hash(block)
    block = mine_block(block, difficulty)
    return block


def add_block(data):
    latest_block = blockchain[-1]
    new_block = create_block(latest_block['index'] + 1, latest_block['hash'], data)
    blockchain.append(new_block)

genesis_block = create_block(0, "0", "Genesis Block")
blockchain.append(genesis_block)

def is_chain_valid(chain, difficulty=4):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]
        
        # Check if current block's previous_hash matches the previous block's hash
        if current_block['previous_hash'] != previous_block['hash']:
            print("Blockchain invalid: Block", current_block['index'], "has incorrect previous hash.")
            return False
        
        # Check if the block's hash is valid
        if current_block['hash'] != calculate_hash(current_block) or not current_block['hash'].startswith('0' * difficulty):
            print("Blockchain invalid: Block", current_block['index'], "hash is invalid.")
            return False
    
    print("Blockchain is valid.")
    return True

add_block("Block 1 Data")
add_block("Block 2 Data")

for block in blockchain:
    print("Block Index:", block['index'])
    print("Timestamp:", block['timestamp'])
    print("Data:", block['data'])
    print("Previous Hash:", block['previous_hash'])
    print("Hash:", block['hash'])
    print("Nonce:", block['nonce'])
    print("-" * 30)

is_chain_valid(blockchain)