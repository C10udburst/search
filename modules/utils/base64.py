from typing import List

from classes import Module, Result, KeywordModule
from re import sub
import base64


class Base64DecodeModule(Module):
    def __init__(self):
        super().__init__("Base64 Decode",
                         "Decode ASCII string using the standard Base64 alphabet.")

    async def search(self, query) -> List[Result]:
        if not sub("\\s", "", query):
            return []
        decoded = base64.b64decode(query).decode('utf-8')
        return [Result(title="Base64 decoding",
                       summary=f"`{decoded}`", weight=7)]


class Base64EncodeModule(KeywordModule):
    def __init__(self):
        super().__init__("Base64 Encode", "Encode ASCII string using the standard Base64 alphabet.", [
            "b64", "base64", "b64encode"
        ])

    async def whitelisted_search(self, query: str) -> List[Result]:
        encoded = base64.b64encode(query.encode('utf-8')).decode('utf-8')
        return [Result(title="Base64 encoding",
                       summary=f"`{encoded}`", weight=9)]


base64_modules = {Base64DecodeModule(), Base64EncodeModule()}
