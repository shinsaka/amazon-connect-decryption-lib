import logging
import boto3
from aws_encryption_sdk import EncryptionSDKClient
from aws_encryption_sdk import CommitmentPolicy
from aws_encryption_sdk.key_providers.raw import RawMasterKey, RawMasterKeyProvider, WrappingKey
from aws_encryption_sdk.identifiers import EncryptionKeyType, WrappingAlgorithm
from aws_encryption_sdk.exceptions import AWSEncryptionSDKClientError

_LOGGER = logging.getLogger(__name__)


class AmazonConnectKeyProviderError(AWSEncryptionSDKClientError):
    """ AmazonConnectKeyProvider Exception """


class AmazonConnectKey(RawMasterKey):
    def decrypt_data_key(self, encrypted_data_key, algorithm, encryption_context):
        self.key_id = encrypted_data_key.key_provider.key_info
        return super().decrypt_data_key(encrypted_data_key, algorithm, encryption_context)


class AmazonConnectKeyProvider(RawMasterKeyProvider):
    _master_key_class = AmazonConnectKey
    provider_id = 'AmazonConnect'

    def prepare_key(self, ssm_parameter_name):
        if not ssm_parameter_name:
            raise AmazonConnectKeyProviderError('Not specified ssm parameter name.')

        self._ssm_parameter_name = ssm_parameter_name
        super().add_master_key('')

    def _get_raw_key(self, key_id):
        ssm_client = boto3.client('ssm')
        response = ssm_client.get_parameter(
            Name=self._ssm_parameter_name,
            WithDecryption=True
        )
        if response and 'Parameter' in response:
            return WrappingKey(
                wrapping_algorithm=WrappingAlgorithm.RSA_OAEP_SHA512_MGF1,
                wrapping_key=response['Parameter']['Value'].encode(),
                wrapping_key_type=EncryptionKeyType.PRIVATE
            )

        raise AWSEncryptionSDKClientError('{} can not get Key {}'.format(key_id))


class AmazonConnectEncryptClient(EncryptionSDKClient):
    def __new__(cls, **kwargs):
        kwargs.setdefault('commitment_policy', CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)

        return super().__new__(cls, **kwargs)
