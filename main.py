from src.vigenere import vigenere_encrypt

ENCRYPTION_KEY = "EXAMPLE"
STRING_TO_ENCRYPT = "TESTEROFTHISCIPHER"


def main() -> None:
    """Main function runs encryption process."""

    print(vigenere_encrypt(ENCRYPTION_KEY, STRING_TO_ENCRYPT))


if __name__ == "__main__":
    main()
