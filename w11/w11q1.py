import hashlib

def hashLz(string, lz):
    target = '0' * lz
    nonce = 0

    while True:
        data = (string + str(nonce)).encode()
        hash_result = hashlib.sha256(data).hexdigest()

        if hash_result.startswith(target):
            return hash_result, nonce
        nonce += 1

string = "talha"
lz = 16

hash_result, nonce = hashLz(string, lz)
print("Hash with " + str(lz) + " leading zeros: " + hash_result)
print("Nonce:", nonce)
