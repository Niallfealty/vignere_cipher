from argparse import ArgumentParser

parser = ArgumentParser("""
    This is a command line utility for archaic encryption.

    Error codes:
        1 - Encryption was attempted with an invalid key value
    """)

parser.add_argument("msg",
        help="The message to encrypt/decrypt (settable via options)")

parser.add_argument("--cipher", "-c", type=str,
        help="Pick a cipher to encrypt with, choose from: c(aesar), v(ingere)")

parser.add_argument("--key", "-k", help="Set a key of choice - needs to be chosen consistently with the cipher")

parser.add_argument("--encrypt", "-e", action="store_true",
        help="Run encryption on message with chosen key")

parser.add_argument("--decrypt", "-d", action="store_true",
        help="Run decryption on message with chosen key (-e flag takes precedence)")

if __name__ == "__main__":
    print(parser.parse_args())
