from cryptography.fernet import Fernet

def decrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    """Decrypt the file at `input_path` and write to `output_path`."""
    cipher = Fernet(key)
    with open(input_path, "rb") as f_in:
        encrypted = f_in.read()
    decrypted = cipher.decrypt(encrypted)
    with open(output_path, "wb") as f_out:
        f_out.write(decrypted)
