import pandas as pd

from encryption import generate_encryption_stream

CIPHER_KEY = "KRYPTOS"
ENCRYPTION_KEY = "CIPHER"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
STRING_TO_ENCRYPT = "TESTEROFTHISCIPHER"


def main() -> None:
    """Main function runs encryption process."""

    keyword_letters = [char for char in CIPHER_KEY]
    alphabet_letters = [char for char in ALPHABET]
    encryption_stream = generate_encryption_stream(ENCRYPTION_KEY, STRING_TO_ENCRYPT)
    indexed_alphabet = {chr(i + 65): str(i) for i in range(len(alphabet_letters))}
    indexed_encryption_string = [
        char.replace(char, indexed_alphabet[char]) for char in STRING_TO_ENCRYPT
    ]
    indexed_encryption_stream = [
        char.replace(char, indexed_alphabet[char]) for char in encryption_stream
    ]

    first_vigenere_row = keyword_letters + [
        char for char in alphabet_letters if char not in keyword_letters
    ]
    vigenere_rows = []
    for i in range(len(alphabet_letters)):
        last_letter = first_vigenere_row[-i:]
        next_vigenere_row = first_vigenere_row[0:-i]
        next_vigenere_row[:0] = last_letter
        vigenere_rows.append(next_vigenere_row)

    vigenere_table = pd.DataFrame(
        vigenere_rows, columns=[_ for _ in range(len(alphabet_letters))]
    )
    vigenere_table.to_csv(f"ref/{CIPHER_KEY}_VIGENERE_TABLE.csv")

    encrypted_string = ""
    for idx, col in zip(indexed_encryption_string, indexed_encryption_stream):
        encrypted_string += vigenere_table[int(idx)].iloc[int(col)]

    print(encrypted_string)


if __name__ == "__main__":
    main()
