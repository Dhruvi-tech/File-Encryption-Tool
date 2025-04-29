import pytest
from pathlib import Path
from file_encryption_tool.key_manager import generate_key, load_key
from file_encryption_tool.encryptor import encrypt_file
from file_encryption_tool.decryptor import decrypt_file

def test_encrypt_decrypt(tmp_path):
    key_file = tmp_path / "test_secret.key"
    input_file = tmp_path / "hello.txt"
    input_file.write_text("Hello, Test!")

    generate_key(str(key_file))
    key = load_key(str(key_file))

    enc_file = str(tmp_path / "hello.txt.enc")
    encrypt_file(str(input_file), enc_file, key)
    assert Path(enc_file).exists()

    dec_file = str(tmp_path / "hello_decrypted.txt")
    decrypt_file(enc_file, dec_file, key)
    assert Path(dec_file).read_text() == "Hello, Test!"
