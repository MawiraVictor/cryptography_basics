import secrets
from cryptography.hazmat.primitives.ciphers import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import  hashes
import os

# Symmetric Encryption using AES-GCM funtion
def aes_ed(message):
    key = secrets.token_bytes(32)  # Generate a random 256-bit key
    nonce = secrets.token_bytes(12)  # Generate a random 96-bit nonce
    aes = AESGCM(key)
    
    ciphertext = aes.encrypt(nonce, message, None)  # Encrypt the message
    plaintext = aes.decrypt(ciphertext[:12], ciphertext[12:], None)  # Decrypt the message and give the original message to bytr
    return key.hex(), ciphertext.hex(), plaintext.decode(), plaintext.decode()

if __name__ == "__main__":
    print(aes_ed(" This is AES - testing"))