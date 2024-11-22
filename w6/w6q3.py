def xor_encrypt_decrypt(input_string, key):
    result_chars = []
    
    for char in input_string:
        char_value = ord(char)
        key_value = ord(key)
        xor_value = char_value ^ key_value
        result_char = chr(xor_value)
        result_chars.append(result_char)

    result_string = ''.join(result_chars)
    
    return result_string

original_message = "world"
key = 'K'

encrypted_message = xor_encrypt_decrypt(original_message, key)
print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
