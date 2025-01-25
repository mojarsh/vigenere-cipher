import string

from pandas import DataFrame


def index_string(base_string: str, index: dict) -> list:
    """Replaces each letter in string with numerical index value."""
    return [char.replace(char, index[char]) for char in base_string]


def generate_indexed_alphabet() -> dict:
    """Generates dict with letter keys matching to numerical values 0 - 25, to reference against Vigenere table."""
    return {chr(i + 65): str(i) for i in range(len(string.ascii_uppercase))}


def generate_reverse_indexed_alphabet() -> dict:
    """Generates dict with numerical keys matching to correspoinding letter, to reference against Vigenere table."""
    return {i: chr(i + 65) for i in range(len(string.ascii_uppercase))}


def generate_encryption_stream(encryption_key: str, string_to_encrypt: str) -> str:
    """Uses computation of remainder to generate encryption stream for given encryption key."""
    a, b = divmod(len(string_to_encrypt), len(encryption_key))
    return encryption_key * a + encryption_key[:b]


def generate_vigenere_table() -> DataFrame:
    """Creates Vigenere table used for message encryption and decryption."""

    first_row = list(string.ascii_uppercase)
    vigenere_rows = []
    vigenere_rows.append(first_row)
    i = 1
    while i < len(string.ascii_uppercase):
        next_vigenere_row = first_row[i:]
        list(map(next_vigenere_row.append, first_row[:i]))
        vigenere_rows.append(next_vigenere_row)
        i += 1

    return DataFrame(
        vigenere_rows, columns=[num for num in range(len(string.ascii_uppercase))]
    )


def vigenere_encrypt(encryption_key: str, string_to_encrypt: str) -> str:
    """Encrypts given string using Vigenere table."""
    index = generate_indexed_alphabet()
    encryption_stream = generate_encryption_stream(encryption_key, string_to_encrypt)
    vigenere_table = generate_vigenere_table()
    indexed_plaintext = index_string(string_to_encrypt, index)
    indexed_key_stream = index_string(encryption_stream, index)
    encrypted_string = ""
    for idx, col in zip(indexed_plaintext, indexed_key_stream):
        encrypted_string += vigenere_table[int(idx)].iloc[int(col)]

    return encrypted_string


def vigenere_decrypt(encryption_key: str, string_to_decrypt: str) -> str:
    """Decrypts given string using Vigenere table."""
    index = generate_indexed_alphabet()
    encryption_stream = generate_encryption_stream(encryption_key, string_to_decrypt)
    vigenere_table = generate_vigenere_table()
    indexed_key_stream = index_string(encryption_stream, index)
    reverse_index = generate_reverse_indexed_alphabet()
    decrypted_string = ""
    for idx, col in zip(indexed_key_stream, string_to_decrypt):
        decrypted_index = vigenere_table[vigenere_table[int(idx)] == col].index.values[
            0
        ]

        decrypted_letter = reverse_index[int(decrypted_index)]
        decrypted_string += decrypted_letter

    return decrypted_string
