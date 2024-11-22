import hashlib
message = "Hello, World!"
digest = hashlib.sha1(message.encode()).hexdigest()
print(f"SHA-1 Digest: {digest}")
