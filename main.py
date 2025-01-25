import click

from src.vigenere import vigenere_decrypt, vigenere_encrypt


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--key",
    help="Encryption key for the Vigenere cipher.",
    type=str,
)
@click.option(
    "--text",
    help="Plain text to encrypt/decrypt.",
    type=str,
)
def encrypt(key, text):
    encrypted_text = vigenere_encrypt(key, text)
    click.echo(encrypted_text)


@cli.command()
@click.option(
    "--key",
    help="Encryption key for the Vigenere cipher.",
    type=str,
)
@click.option(
    "--text",
    help="Plain text to encrypt/decrypt.",
    type=str,
)
def decrypt(key, text):
    decrypted_text = vigenere_decrypt(key, text)
    click.echo(decrypted_text)


if __name__ == "__main__":
    cli()
