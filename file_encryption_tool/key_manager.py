from cryptography.fernet import Fernet

def generate_key(output_path):
    key = Fernet.generate_key()
    with open(output_path, "wb") as key_file:
        key_file.write(key)

def load_key(key_path):
    with open(key_path, "rb") as key_file:
        return key_file.read()
