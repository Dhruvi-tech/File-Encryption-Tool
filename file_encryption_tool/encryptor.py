from cryptography.fernet import Fernet

def encrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    """Encrypt the file at `input_path` and write to `output_path`."""
    cipher = Fernet(key)
    with open(input_path, "rb") as f_in:
        data = f_in.read()
    encrypted = cipher.encrypt(data)
    with open(output_path, "wb") as f_out:
        f_out.write(encrypted)
