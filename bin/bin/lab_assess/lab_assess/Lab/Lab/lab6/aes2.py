from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES block size is 16 bytes
BLOCK_SIZE = 16

# Function to encrypt message using AES (ECB mode)
def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Create a new AES cipher object in ECB mode
    padded_message = pad(message.encode(), BLOCK_SIZE)  # Pad message to be a multiple of BLOCK_SIZE
    encrypted_message = cipher.encrypt(padded_message)  # Encrypt the padded message
    return encrypted_message

# Function to decrypt message using AES (ECB mode)
def aes_decrypt(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Create a new AES cipher object in ECB mode
    decrypted_message = unpad(cipher.decrypt(encrypted_message), BLOCK_SIZE)  # Decrypt and unpad the message
    return decrypted_message.decode()

# Example usage
# Step 1: Generate a random 16-byte AES key
key = get_random_bytes(16)

# Step 2: Define a message to encrypt
message = "HELLO AES"

# Step 3: Encrypt the message
encrypted_message = aes_encrypt(message, key)
print(f"Encrypted Message (in bytes): {encrypted_message}")

# Step 4: Decrypt the message
decrypted_message = aes_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
