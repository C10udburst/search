from typing import List
import hashlib

from classes import KeywordModule, Result


class HashModule(KeywordModule):
    def __init__(self, algorithm: str):
        super().__init__(f"Hash {algorithm.upper()}", f"Hashes given string using `{algorithm.lower()}`.", [
            algorithm.lower(),
            algorithm.lower().replace("_", ""),
            "hash",
            "hashing"
        ])
        self.algorithm = algorithm

    async def whitelisted_search(self, query: str) -> List[Result]:
        h = hashlib.new(self.algorithm)
        h.update(query.encode('utf-8'))
        result = h.hexdigest()
        return [
            Result(
                title=f"{self.algorithm.upper()} hashing",
                summary=f"`{result}`",
                color=0xffd343,
                weight=9
            )
        ]
