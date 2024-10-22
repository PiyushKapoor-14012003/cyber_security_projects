from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class DESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_text):
        cipher = DES.new(self.key, DES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode(), DES.block_size))
        iv = cipher.iv
        return iv + ct_bytes

    def decrypt(self, cipher_text):
        iv = cipher_text[:DES.block_size]
        ct = cipher_text[DES.block_size:]
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), DES.block_size)
        return pt.decode()

class DESManager:
    def __init__(self, key_length=8):
        self.key = get_random_bytes(key_length)
        self.cipher = DESCipher(self.key)

    def encrypt_message(self, message):
        return self.cipher.encrypt(message)

    def decrypt_message(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message)

# Example usage
des_manager = DESManager()
plain_text = input("Enter the text to encrypt: ")
print(f"Plain Text: {plain_text}")
cipher_text = des_manager.encrypt_message(plain_text)
print(f"Cipher Text: {cipher_text}")

decrypted_text = des_manager.decrypt_message(cipher_text)
print(f"Decrypted Text: {decrypted_text}")