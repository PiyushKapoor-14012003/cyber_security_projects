from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_text):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
        iv = cipher.iv
        return iv + ct_bytes

    def decrypt(self, cipher_text):
        iv = cipher_text[:AES.block_size]
        ct = cipher_text[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode()

class AESManager:
    def __init__(self, key_length=16):
        self.key = get_random_bytes(key_length)
        self.cipher = AESCipher(self.key)

    def encrypt_message(self, message):
        return self.cipher.encrypt(message)

    def decrypt_message(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message)

# Example usage
aes_manager = AESManager()
plain_text = input("Enter the text to encrypt: ")
print(f"Plain Text: {plain_text}")
cipher_text = aes_manager.encrypt_message(plain_text)
print(f"Cipher Text: {cipher_text}")

decrypted_text = aes_manager.decrypt_message(cipher_text)
print(f"Decrypted Text: {decrypted_text}")