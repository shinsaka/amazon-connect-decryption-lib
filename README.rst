# amazon-connect-dencryption-lib

## Required

- Python 3.8+
- aws-encryption-sdk
- boto3

## Install

```
$ pip install amazon-connect-decryption-lib
```

## Usage

```python
from amazon-connect-dencryption-lib import decrypt

ssm_parameter_name = 'CONNECT_INPUT_DECRYPTION_KEY'
encrypted_text_bin = base64.b64decode(encrypted_text)

plain_text = decrypt(ssm_parameter_name, encrypted_text_bin)

```
