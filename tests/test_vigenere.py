from src.vigenere import (
    generate_encryption_stream,
    generate_indexed_alphabet,
    generate_vigenere_table,
    index_string,
    vigenere_encrypt,
)

ENCRYPTION_KEY = "EXAMPLE"
STRING_TO_ENCRYPT = "TESTEROFTHISCIPHER"


def test_string_indexing() -> None:
    indexed_alphabet = generate_indexed_alphabet()
    indexed_string = index_string(base_string="DCBA", index=indexed_alphabet)
    assert indexed_string == ["3", "2", "1", "0"]


def test_encryption_stream_generation() -> None:
    assert (
        generate_encryption_stream(ENCRYPTION_KEY, STRING_TO_ENCRYPT)
        == "EXAMPLEEXAMPLEEXAM"
    )


def test_generate_indexed_alphabet() -> None:
    index = generate_indexed_alphabet()
    assert index["A"] == "0"


def test_vigenere_table() -> None:
    assert generate_vigenere_table().shape == (26, 26)


def test_encryption() -> None:
    assert vigenere_encrypt(ENCRYPTION_KEY, STRING_TO_ENCRYPT) == "PHSHPGKBWHWDRELKEF"
