import string

from src.vigenere import VigenereCipher

CIPHER_KEY = "TEST"
ENCRYPTION_KEY = "EXAMPLE"

indexed_alphabet = {chr(i + 65): str(i) for i in range(len(string.ascii_uppercase))}
vigenere = VigenereCipher(CIPHER_KEY, ENCRYPTION_KEY)


def test_vigenere_cipher_instance() -> None:
    assert isinstance(vigenere, VigenereCipher)


def test_string_indexing() -> None:
    indexed_string = vigenere.index_string(base_string="DCBA", index=indexed_alphabet)
    assert indexed_string == ["3", "2", "1", "0"]


def test_encryption_stream_generation() -> None:
    assert vigenere.generate_encryption_stream("TESTSTRING") == "EXAMPLEEXA"
