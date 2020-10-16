import base64
from .amazon_connect_dencryption_lib import (
    AmazonConnectEncryptClient,
    AmazonConnectKeyProviderError,
    AmazonConnectKeyProvider,
)


__version__ = '0.1.0'

__all__ = [
    'AmazonConnectEncryptClient',
    'AmazonConnectKeyProviderError',
    'AmazonConnectKeyProvider',
]


def dencrypt(ssm_parameter_name, encrypted_text):
    """
    dencrypt shortcut function
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
