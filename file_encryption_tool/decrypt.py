from cryptography.fernet import Fernet

def decrypt_file(input_path, output_path, key):
    with open(input_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_path, "wb") as file:
        file.write(decrypted_data)
