==============================
amazon-connect-dencryption-lib
==============================

.. image:: https://pepy.tech/badge/amazon-connect-decryption-lib
   :target: https://pepy.tech/project/amazon-connect-decryption-lib

Required
========

* Python 3.8+
* https://github.com/aws/aws-encryption-sdk-python/
* boto3

Install
========

.. code-block::

    $ pip install amazon-connect-decryption-lib



Usage
=======

.. code-block:: python

    from amazon_connect_decryption_lib import decrypt

    ssm_parameter_name = 'CONNECT_INPUT_DECRYPTION_KEY'
    encrypted_text = 'AYADeOCM0sgyKxALhzT1Q0fD+FEAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREFxdnNLME55K1J1R3JSR0lLdmFuSVp5Q254RHpNMTY0ZUx4SUt0RE80czR1QWhKRlV2Tm44VExic0p1UnIvb2FnQT09AAEADUFtYXpvbkNvbm5lY3QAJGE1ZWNkNzQ5LTRiZDgtNGE5NC1iZmRlLTI3ZWVmZTRmMTJiMQIAfQ/ZWMphr1+3+vAd9REB07pMkNP4bgQSamOzwmSHX7B3Fx5GX1wlbkys9yC//5WfUy7ikFKVsy1BpyyGZ3gtkw8+etXt6c/TIScjxHP+4pXFGVHPwTeAPNNERMJwu3P5DyZEEflCDIpP6EtcCBlWgNAu4bOTxEDmUdesR1M3xy/BmIK/daUY9A6Z35NKmS1rV3L8kxPwvLzi93m2vwH1YGXcDcxuL3Iwc6YoTpI0ZIpQtNs30yeYBm1NNW3No76Wq6+dxNTRs5O6moaS0SNYoPrVmBImU7xqvHKoiBJeRxyA20rRPNbyrAZw3kcoLxyuhSqcJJS1NKpuUY/XO4i/xMa5C+ZtzfWbsiUF4ApGzkEVZ/m5iMTIFwI6BVlTV60wVMZkqSaQSnJpoC/qOdWK78LxxdBdmL470lWze0J35Wy7VXynpPAqq9tFYA6Lfq2OyOfjDxj1hwOcaIvjO3yeWCH8SPjer6NChYUUWhLt0CObxaJcHyH5YogzknLyiBAvfvVmlJgP8HcLKg8mJM0GQ+aEokISp9HNIyvFqDTwXsRz2OIdOE2a9qrDirkYC/+HEbkka/hYl4nYr+n+Knn/0RCQ8Nwb7oYk7WnZlU1ADCmYIKjotor2hEK/TlcuxXLylJj8ofgbe8HbsEjFMBdG442b1Eun4r4nUZuLZfm33ncCAAAAAAwAABAAxVaVGO1V9GzHfrF+z1YV08Baa+e9WeAKBoDFiP////8AAAAB4doeJ2gezq6CHwv+AAAADMznKid/99jwAREvH4WZtUbQSJSINk1Jes+EmT8AZzBlAjBdmQ6tP1SFucy/R6YrhrTR29AeBK3qF50WMOZ+TC55Yk3J+QAxy3HhSF4zI6mXn5kCMQC2sBABuFsktmfEvfr1EVWGPGtDYaXEk72ZBR6r3TG/opJSaWuoAUkxxAHCUt6gEl4='

    plain_text = decrypt(ssm_parameter_name, encrypted_text)
    print(plain_text)  # output is 112344567789


Usage with AWS Lambda
======================

.. code-block:: python

    from amazon_connect_decryption_lib import decrypt

    def lambda_handler(event, context):
        ssm_parameter_name = 'CONNECT_INPUT_DECRYPTION_KEY'
        encrypted_text = event['Details']['ContactData']['Attributes']['EncryptedNumber']  # EncryptedNumber is your contact attribute name.

        plain_text = decrypt(ssm_parameter_name, encrypted_text)
        print(plain_text)

        return {'DecryptResult': plain_text }


Test(for Developer)
====================

.. code-block::

    $ python -m unittest


