from cryptography.fernet import Fernet

def encrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    """Encrypt the file at `input_path` and write to `output_path`."""
    cipher = Fernet(key)
    with open(input_path, "rb") as f_in:
        data = f_in.read()
    encrypted = cipher.encrypt(data)
    with open(output_path, "wb") as f_out:
        f_out.write(encrypted)
if __name__ == "__main__":
    import argparse
    from key_generator import load_key  # adjust import if needed

    parser = argparse.ArgumentParser(description="Encrypt a file.")
    parser.add_argument("input_file", help="Path to the file to encrypt")
    parser.add_argument("key_file", help="Path to the encryption key")
    parser.add_argument("output_file", help="Path to save the encrypted file")

    args = parser.parse_args()

    key = load_key(args.key_file)

    from file_encryption_tool.encrypt import encrypt_file
    encrypt_file(args.input_file, key, args.output_file)
