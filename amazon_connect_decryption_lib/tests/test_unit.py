import unittest
import base64
from amazon_connect_dencryption_lib import decrypt


class UtilsTests(unittest.TestCase):
    def test_hoge(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()


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

data = 'AYADeOCM0sgyKxALhzT1Q0fD+FEAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREFxdnNLME55K1J1R3JSR0lLdmFuSVp5Q254RHpNMTY0ZUx4SUt0RE80czR1QWhKRlV2Tm44VExic0p1UnIvb2FnQT09AAEADUFtYXpvbkNvbm5lY3QAJGE1ZWNkNzQ5LTRiZDgtNGE5NC1iZmRlLTI3ZWVmZTRmMTJiMQIAfQ/ZWMphr1+3+vAd9REB07pMkNP4bgQSamOzwmSHX7B3Fx5GX1wlbkys9yC//5WfUy7ikFKVsy1BpyyGZ3gtkw8+etXt6c/TIScjxHP+4pXFGVHPwTeAPNNERMJwu3P5DyZEEflCDIpP6EtcCBlWgNAu4bOTxEDmUdesR1M3xy/BmIK/daUY9A6Z35NKmS1rV3L8kxPwvLzi93m2vwH1YGXcDcxuL3Iwc6YoTpI0ZIpQtNs30yeYBm1NNW3No76Wq6+dxNTRs5O6moaS0SNYoPrVmBImU7xqvHKoiBJeRxyA20rRPNbyrAZw3kcoLxyuhSqcJJS1NKpuUY/XO4i/xMa5C+ZtzfWbsiUF4ApGzkEVZ/m5iMTIFwI6BVlTV60wVMZkqSaQSnJpoC/qOdWK78LxxdBdmL470lWze0J35Wy7VXynpPAqq9tFYA6Lfq2OyOfjDxj1hwOcaIvjO3yeWCH8SPjer6NChYUUWhLt0CObxaJcHyH5YogzknLyiBAvfvVmlJgP8HcLKg8mJM0GQ+aEokISp9HNIyvFqDTwXsRz2OIdOE2a9qrDirkYC/+HEbkka/hYl4nYr+n+Knn/0RCQ8Nwb7oYk7WnZlU1ADCmYIKjotor2hEK/TlcuxXLylJj8ofgbe8HbsEjFMBdG442b1Eun4r4nUZuLZfm33ncCAAAAAAwAABAAxVaVGO1V9GzHfrF+z1YV08Baa+e9WeAKBoDFiP////8AAAAB4doeJ2gezq6CHwv+AAAADMznKid/99jwAREvH4WZtUbQSJSINk1Jes+EmT8AZzBlAjBdmQ6tP1SFucy/R6YrhrTR29AeBK3qF50WMOZ+TC55Yk3J+QAxy3HhSF4zI6mXn5kCMQC2sBABuFsktmfEvfr1EVWGPGtDYaXEk72ZBR6r3TG/opJSaWuoAUkxxAHCUt6gEl4='

print(dencrypt(data))


