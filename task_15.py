from typing import Iterator


class BlockTranspositionCipher:
    def __init__(self, text: str, key: str, decrypt: bool = False):
        self._validate_key(key)

        self._text = text
        self._key = key.lower()
        self._decrypt = decrypt

    def __iter__(self) -> Iterator[str]:
        self._blocks = self._split_into_blocks()
        self._order = self._build_order()

        self._index = 0
        return self

    def __next__(self) -> str:
        if self._index >= len(self._blocks):
            raise StopIteration

        block = self._blocks[self._index]
        self._index += 1

        if self._decrypt:
            return self._decrypt_block(block)
        return self._encrypt_block(block)

    @staticmethod
    def _validate_key(key: str) -> None:
        if not key.isalpha():
            raise ValueError("Key must contain only English letters")

        lowered = key.lower()
        if len(set(lowered)) != len(lowered):
            raise ValueError("Key must contain unique letters")

    def _build_order(self) -> list[int]:
        min_char = min([ord(char) for char in self._key])
        return [ord(char) - min_char for char in self._key]

    def _split_into_blocks(self) -> list[str]:
        blocks = []
        block_size = len(self._key)
        for i in range(0, len(self._text), block_size):
            block = self._text[i:i + block_size]
            if len(block) < block_size:
                block += " " * (block_size - len(block))
            blocks.append(block)
        return blocks

    def _encrypt_block(self, block: str) -> str:
        return "".join(block[i] for i in self._order)

    def _decrypt_block(self, block: str) -> str:
        result = [""] * len(self._key)
        for original_index, encrypted_index in enumerate(self._order):
            result[encrypted_index] = block[original_index]
        return "".join(result)
