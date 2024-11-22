import hashlib
message = "Hello, World!"
digest = hashlib.md5(message.encode()).hexdigest()
print(f"MD5: {digest}")
