from cryptography.fernet import Fernet

def generate_key(path: str = "secret.key") -> None:
    """Generate a new Fernet key and save it to `path`."""
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)

def load_key(path: str = "secret.key") -> bytes:
    """Load an existing key from `path`."""
    with open(path, "rb") as f:
        return f.read()
