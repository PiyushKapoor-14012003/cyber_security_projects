from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

class RSACipher:
    def __init__(self, key_pair):
        self.key_pair = key_pair
        self.public_key = key_pair.publickey()
        self.cipher_encrypt = PKCS1_OAEP.new(self.public_key)
        self.cipher_decrypt = PKCS1_OAEP.new(self.key_pair)

    def encrypt(self, plain_text):
        return self.cipher_encrypt.encrypt(plain_text.encode())

    def decrypt(self, cipher_text):
        return self.cipher_decrypt.decrypt(cipher_text).decode()

class RSAManager:
    def __init__(self, key_length=2048):
        self.key_pair = RSA.generate(key_length)
        self.cipher = RSACipher(self.key_pair)

    def encrypt_message(self, message):
        return self.cipher.encrypt(message)

    def decrypt_message(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message)

# Example usage
rsa_manager = RSAManager()
plain_text = input("Enter the text to encrypt: ")
print(f"Plain Text: {plain_text}")
cipher_text = rsa_manager.encrypt_message(plain_text)
print(f"Cipher Text: {cipher_text}")

decrypted_text = rsa_manager.decrypt_message(cipher_text)
print(f"Decrypted Text: {decrypted_text}") 