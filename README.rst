# amazon-connect-dencryption-lib

## Required

- Python 3.8+
- aws-encryption-sdk
- boto3

## Install

```
$ pip install ac-dencryption-lib
```

## Usage

```python
import base64
from amazon-connect-dencryption-lib import (
    AmazonConnectKeyProvider,
    AmazonConnectEncryptClient,
)

def dencrypt(encrypted_text):
    ssm_parameter_name = 'CONNECT_INPUT_DECRYPTION_KEY'
    encrypted_text_bin = base64.b64decode(encrypted_text)

    ammazon_connect_key_provider = AmazonConnectKeyProvider()
    ammazon_connect_key_provider.prepare_key(ssm_parameter_name)

    client = AmazonConnectEncryptClient()
    plaintext, _ = client.decrypt(
        source=encrypted_text_bin,
        key_provider=ammazon_connect_key_provider
    )

    return plaintext

```
