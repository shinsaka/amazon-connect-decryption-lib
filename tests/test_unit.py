import unittest
import boto3
from moto import mock_ssm

class DecryptTests(unittest.TestCase):
    @mock_ssm
    def test_decrypt(self):
        from amazon_connect_decryption_lib import decrypt

        # put private-key to ssm parameter
        with open('./tests/test.private.key') as fp:
            pk = fp.read()
        c = boto3.client('ssm')
        c.put_parameter(
            Name='PARAM_NAME',
            Type='SecureString',
            Value=pk
        )

        # success decrypt
        data = 'AYADeOCM0sgyKxALhzT1Q0fD+FEAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREFxdnNLME55K1J1R3JSR0lLdmFuSVp5Q254RHpNMTY0ZUx4SUt0RE80czR1QWhKRlV2Tm44VExic0p1UnIvb2FnQT09AAEADUFtYXpvbkNvbm5lY3QAJGE1ZWNkNzQ5LTRiZDgtNGE5NC1iZmRlLTI3ZWVmZTRmMTJiMQIAfQ/ZWMphr1+3+vAd9REB07pMkNP4bgQSamOzwmSHX7B3Fx5GX1wlbkys9yC//5WfUy7ikFKVsy1BpyyGZ3gtkw8+etXt6c/TIScjxHP+4pXFGVHPwTeAPNNERMJwu3P5DyZEEflCDIpP6EtcCBlWgNAu4bOTxEDmUdesR1M3xy/BmIK/daUY9A6Z35NKmS1rV3L8kxPwvLzi93m2vwH1YGXcDcxuL3Iwc6YoTpI0ZIpQtNs30yeYBm1NNW3No76Wq6+dxNTRs5O6moaS0SNYoPrVmBImU7xqvHKoiBJeRxyA20rRPNbyrAZw3kcoLxyuhSqcJJS1NKpuUY/XO4i/xMa5C+ZtzfWbsiUF4ApGzkEVZ/m5iMTIFwI6BVlTV60wVMZkqSaQSnJpoC/qOdWK78LxxdBdmL470lWze0J35Wy7VXynpPAqq9tFYA6Lfq2OyOfjDxj1hwOcaIvjO3yeWCH8SPjer6NChYUUWhLt0CObxaJcHyH5YogzknLyiBAvfvVmlJgP8HcLKg8mJM0GQ+aEokISp9HNIyvFqDTwXsRz2OIdOE2a9qrDirkYC/+HEbkka/hYl4nYr+n+Knn/0RCQ8Nwb7oYk7WnZlU1ADCmYIKjotor2hEK/TlcuxXLylJj8ofgbe8HbsEjFMBdG442b1Eun4r4nUZuLZfm33ncCAAAAAAwAABAAxVaVGO1V9GzHfrF+z1YV08Baa+e9WeAKBoDFiP////8AAAAB4doeJ2gezq6CHwv+AAAADMznKid/99jwAREvH4WZtUbQSJSINk1Jes+EmT8AZzBlAjBdmQ6tP1SFucy/R6YrhrTR29AeBK3qF50WMOZ+TC55Yk3J+QAxy3HhSF4zI6mXn5kCMQC2sBABuFsktmfEvfr1EVWGPGtDYaXEk72ZBR6r3TG/opJSaWuoAUkxxAHCUt6gEl4='
        self.assertEqual(decrypt('PARAM_NAME', data), '112344567789')

        # exception decrypt (not found ssm parameter)
        with self.assertRaises(Exception):
            self.assertEqual(decrypt('PARAM_NAME_NOENTRY', data), '112344567789')

        # exception decrypt (not found ssm parameter)
        from amazon_connect_decryption_lib import AmazonConnectKeyProviderError
        with self.assertRaises(AmazonConnectKeyProviderError):
            self.assertEqual(decrypt('', data), '112344567789')

if __name__ == '__main__':
    unittest.main()
