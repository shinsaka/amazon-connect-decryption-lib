import base64
from .core import AmazonConnectEncryptClient, AmazonConnectKeyProvider


def decrypt(ssm_parameter_name, encrypted_text):
    """
    decrypt shortcut function
    """
    encrypted_text_bin = base64.b64decode(encrypted_text)

    ammazon_connect_key_provider = AmazonConnectKeyProvider()
    ammazon_connect_key_provider.prepare_key(ssm_parameter_name)

    client = AmazonConnectEncryptClient()
    plaintext, _ = client.decrypt(
        source=encrypted_text_bin,
        key_provider=ammazon_connect_key_provider
    )

    return plaintext.decode()
