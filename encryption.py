import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import os

#  Symmetric Encryption using AES-GCM function
def aes_ed(message):
    key = secrets.token_bytes(32)  # Generate a random 256-bit key
    nonce = secrets.token_bytes(12)  # Generate a random 96-bit nonce
    aes = AESGCM(key)
    
    # Encrypt the message
    ciphertext = aes.encrypt(nonce, message.encode(), None)
    
    # Decrypt the message - use the same nonce and full ciphertext
    plaintext = aes.decrypt(nonce, ciphertext, None)
    
    return key.hex(), ciphertext.hex(), plaintext.decode()

# Asymmetric Encryption using RSA function
def rsa_ed(message):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(   # Optimal Asymmetric Encryption Padding
            mgf=padding.MGF1(algorithm=hashes.SHA256()),   # mask generation function
            algorithm=hashes.SHA256(),   # hashing algorithm
            label=None 
        )
    )
    
    plaintext = private_key.decrypt(   # decrypting the ciphertext
        ciphertext,  # the ciphertext to decrypt
        padding.OAEP(  # Optimal Asymmetric Encryption Padding
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )        
    )
    return ciphertext.hex(), plaintext.decode()

if __name__ == "__main__":
    print("AES Encryption/Decryption:")
    key_hex, ciphertext_hex, plaintext = aes_ed("This is AES - testing")
    print(f"Key: {key_hex}")
    print(f"Ciphertext: {ciphertext_hex}")
    print(f"Plaintext: {plaintext}")
    print()
    
    print("RSA Encryption/Decryption:")
    rsa_ciphertext, rsa_plaintext = rsa_ed("This is RSA - testing")
    print(f"Ciphertext: {rsa_ciphertext}")
    print(f"Plaintext: {rsa_plaintext}")