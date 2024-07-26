class VigenereCipher:
    def __init__(self, cipher_key: str, encryption_key: str):
        self.cipher_key = cipher_key
        self.encryption_key = encryption_key

    def index_string(self, base_string: str, index: dict) -> list:
        """Replaces each letter in string with numerical index value."""
        return [char.replace(char, index[char]) for char in base_string]

    def generate_encryption_stream(self, string_to_encrypt: str) -> str:
        """Uses computation of remainder to generate encryption stream for given encryption key."""
        a, b = divmod(len(string_to_encrypt), len(self.encryption_key))
        return self.encryption_key * a + self.encryption_key[:b]
