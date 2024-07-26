import string

import pandas as pd

from src.vigenere import VigenereCipher

CIPHER_KEY = "KRYPTOS"
ENCRYPTION_KEY = "CIPHER"
STRING_TO_ENCRYPT = "TESTEROFTHISCIPHER"


def main() -> None:
    """Main function runs encryption process."""

    vigenere = VigenereCipher(CIPHER_KEY, ENCRYPTION_KEY)
    encryption_stream = vigenere.generate_encryption_stream(
        string_to_encrypt=STRING_TO_ENCRYPT
    )
    indexed_alphabet = {chr(i + 65): str(i) for i in range(len(string.ascii_uppercase))}
    indexed_encryption_string = vigenere.index_string(
        STRING_TO_ENCRYPT, indexed_alphabet
    )
    indexed_encryption_stream = vigenere.index_string(
        encryption_stream, indexed_alphabet
    )

    first_vigenere_row = list(CIPHER_KEY) + [
        char for char in list(string.ascii_uppercase) if char not in list(CIPHER_KEY)
    ]
    vigenere_rows = []
    for i in range(len(string.ascii_uppercase)):
        last_letter = first_vigenere_row[-i:]
        next_vigenere_row = first_vigenere_row[0:-i]
        next_vigenere_row[:0] = last_letter
        vigenere_rows.append(next_vigenere_row)

    vigenere_table = pd.DataFrame(
        vigenere_rows, columns=[_ for _ in range(len(string.ascii_uppercase))]
    )
    vigenere_table.to_csv(f"ref/{CIPHER_KEY}_VIGENERE_TABLE.csv")

    encrypted_string = ""
    for idx, col in zip(indexed_encryption_string, indexed_encryption_stream):
        encrypted_string += vigenere_table[int(idx)].iloc[int(col)]

    print(encrypted_string)


if __name__ == "__main__":
    main()
