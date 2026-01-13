import pytest

from task_15 import BlockTranspositionCipher


def test_full_encryption_example():
    text = "HELLOWORLD"
    key = "bAc"

    cipher = BlockTranspositionCipher(text, key)
    encrypted = "".join(cipher)

    assert encrypted == "EHLOLWROL D "


@pytest.mark.parametrize(
    "text, key",
    [
        ("HELLOWORLD", "acb"),
        ("python", "zxy"),
        ("short", "abc"),
        ("WITH SPACES", "cab"),
        ("helloworld", "fhij"),
    ],
)
def test_encrypt_decrypt_roundtrip(text, key):
    cipher = BlockTranspositionCipher(text, key)
    encrypted = "".join(cipher)

    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    decrypted = "".join(decipher)

    assert decrypted.rstrip() == text
