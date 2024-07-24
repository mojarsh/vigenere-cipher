def generate_encryption_stream(encryption_key: str, string_to_encrypt: str) -> str:
    """Uses computation of remainder to generate encryption stream for given encryption key."""
    a, b = divmod(len(string_to_encrypt), len(encryption_key))
    return encryption_key * a + encryption_key[:b]
