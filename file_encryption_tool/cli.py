import argparse
from file_encryption_tool.key_manager import generate_key, load_key
from file_encryption_tool.encryptor import encrypt_file
from file_encryption_tool.decryptor import decrypt_file

def main():
    parser = argparse.ArgumentParser(description="File Encryption/Decryption Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    gen_parser = subparsers.add_parser("generate-key", help="Generate a secret key")
    gen_parser.add_argument("-o", "--output", default="secret.key", help="Path to save the generated key")

    enc_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    enc_parser.add_argument("input", help="Input file path to encrypt")
    enc_parser.add_argument("-o", "--output", help="Encrypted file output path (default: <input>.enc)")
    enc_parser.add_argument("-k", "--key", default="secret.key", help="Path to the secret key file")

    dec_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    dec_parser.add_argument("input", help="Encrypted file path (.enc)")
    dec_parser.add_argument("-o", "--output", help="Decrypted file output path (default: replace .enc with _decrypted)")
    dec_parser.add_argument("-k", "--key", default="secret.key", help="Path to the secret key file")

    args = parser.parse_args()

    if args.command == "generate-key":
        generate_key(args.output)
        print(f"Key generated and saved to {args.output}")
    elif args.command == "encrypt":
        key = load_key(args.key)
        out = args.output or args.input + ".enc"
        encrypt_file(args.input, out, key)
        print(f"Encrypted {args.input} to {out}")
    elif args.command == "decrypt":
        key = load_key(args.key)
        out = args.output or args.input.replace(".enc", "_decrypted")
        decrypt_file(args.input, out, key)
        print(f"Decrypted {args.input} to {out}")

if __name__ == "__main__":
    main()
