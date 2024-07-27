import string

from pandas import DataFrame


def index_string(base_string: str, index: dict) -> list:
    """Replaces each letter in string with numerical index value."""
    return [char.replace(char, index[char]) for char in base_string]


def generate_indexed_alphabet() -> dict:
    """Generates dict with letter keys matching to numerical values 0 - 25, to reference against Vigenere table."""
    return {chr(i + 65): str(i) for i in range(len(string.ascii_uppercase))}


def generate_encryption_stream(encryption_key: str, string_to_encrypt: str) -> str:
    """Uses computation of remainder to generate encryption stream for given encryption key."""
    a, b = divmod(len(string_to_encrypt), len(encryption_key))
    return encryption_key * a + encryption_key[:b]


def generate_vigenere_table() -> DataFrame:
    """Creates Vigenere table used for message encryption and decryption."""

    first_row = list(string.ascii_uppercase)
    vigenere_rows = []
    for i in range(len(string.ascii_uppercase)):
        last_letter = first_row[-i:]
        next_vigenere_row = first_row[0:-i]
        next_vigenere_row[:0] = last_letter
        vigenere_rows.append(next_vigenere_row)

    return DataFrame(
        vigenere_rows, columns=[num for num in range(len(string.ascii_uppercase))]
    )


def vigenere_encrypt(encryption_key: str, string_to_encrypt: str) -> str:
    """Encrypts given string using Vigenere table."""
    index = generate_indexed_alphabet()
    encryption_stream = generate_encryption_stream(encryption_key, string_to_encrypt)
    vigenere_table = generate_vigenere_table()
    indexed_encryption_string = index_string(string_to_encrypt, index=index)
    indexed_encryption_stream = index_string(encryption_stream, index=index)
    encrypted_string = ""
    for idx, col in zip(indexed_encryption_string, indexed_encryption_stream):
        encrypted_string += vigenere_table[int(idx)].iloc[int(col)]

    return encrypted_string


def vigenere_decrypt() -> str:
    pass
