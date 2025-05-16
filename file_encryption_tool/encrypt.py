import os
import hashlib
import base64
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_key(password: str = None, salt: bytes = None) -> tuple:
    """Generate a Fernet key. If password is provided, derive key using PBKDF2."""
    if password:
        if not salt:
            salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt
    else:
        return Fernet.generate_key(), None

def save_key(key: bytes, path: str, salt: bytes = None):
    with open(path, "wb") as key_file:
        key_file.write(key)
        if salt:
            key_file.write(b"\n" + salt)

def load_key(path: str):
    with open(path, "rb") as key_file:
        lines = key_file.readlines()
        key = lines[0].strip()
        salt = lines[1].strip() if len(lines) > 1 else None
        return key, salt

def get_file_hash(path: str) -> str:
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def encrypt_file(input_path, output_path, key, metadata=True):
    try:
        with open(input_path, "rb") as file:
            data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        if metadata:
            file_hash = hashlib.sha256(data).hexdigest()
            meta = {
                "original_filename": os.path.basename(input_path),
                "sha256": file_hash
            }
            meta_json = json.dumps(meta).encode() + b"\n"
            encrypted_data = meta_json + encrypted_data
        with open(output_path, "wb") as file:
            file.write(encrypted_data)
        print(f"Encryption successful. SHA256: {file_hash}")
    except Exception as e:
        print(f"Encryption failed: {e}")

def decrypt_file(input_path, output_path, key, metadata=True):
    try:
        with open(input_path, "rb") as file:
            if metadata:
                meta_json = b""
                while True:
                    c = file.read(1)
                    if c == b"\n": break
                    meta_json += c
                meta = json.loads(meta_json.decode())
            encrypted_data = file.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(output_path, "wb") as file:
            file.write(decrypted_data)
        if metadata:
            file_hash = hashlib.sha256(decrypted_data).hexdigest()
            print(f"Decryption successful. SHA256: {file_hash}")
            if file_hash == meta["sha256"]:
                print("File integrity verified.")
            else:
                print("Warning: File hash mismatch! Integrity compromised.")
        else:
            print("Decryption successful.")
    except Exception as e:
        print(f"Decryption failed: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt or decrypt files with Fernet.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"])
    parser.add_argument("input", help="Input file path")
    parser.add_argument("output", help="Output file path")
    parser.add_argument("--keyfile", help="Path to save/load the encryption key", required=True)
    parser.add_argument("--password", help="Password for key derivation")
    args = parser.parse_args()

    if args.mode == "encrypt":
        if args.password:
            key, salt = generate_key(args.password)
        else:
            key, salt = generate_key()
        save_key(key, args.keyfile, salt)
        encrypt_file(args.input, args.output, key)
    else:
        key, salt = load_key(args.keyfile)
        if salt and args.password:
            key, _ = generate_key(args.password, salt)
        decrypt_file(args.input, args.output, key)
