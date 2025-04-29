# File-Encryption-Tool
# 🔐 File Encryption/Decryption Tool

A Python CLI for encrypting and decrypting files using the `cryptography` library (Fernet).

## Features
- Generate and manage secret keys
- Encrypt any file
- Decrypt `.enc` files
- Modular code structure

## Installation
```bash
git clone https://github.com/your-username/file-encryption-tool.git
cd file-encryption-tool
pip install -r requirements.txt
```

## Usage
```bash
# Generate a key
python -m file_encryption_tool.cli generate-key -o mykey.key

# Encrypt a file
python -m file_encryption_tool.cli encrypt secret.txt -k mykey.key -o secret.txt.enc

# Decrypt a file
python -m file_encryption_tool.cli decrypt secret.txt.enc -k mykey.key -o secret_decrypted.txt
```

## Testing
```bash
pytest
```

## License
MIT
