# Import the cryptography Library
from cryptography.fernet import Fernet

# Generate a Fernet Key
key = Fernet.generate_key()

# Print the key
print("Açarınız...\n", key.decode())

# Get the input text
input_text = input("Şifrələnəcək mətni daxil edin...\n")

# Encrypt the text
encrypted_text = Fernet(key).encrypt(input_text.encode())

# Print the encrypted text
print("Şifrələnmiş mətn...\n", encrypted_text.decode())
