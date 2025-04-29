from cryptography.fernet import Fernet

def encrypt_file(input_path, output_path, key):
    with open(input_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(output_path, "wb") as file:
        file.write(encrypted_data)
