from typing import List

from classes import Module, Result
from . import async_cse
from modules.google.utils import create_result
from .keys import API_KEYS


class GoogleModule(Module):
    def __init__(self):
        super().__init__("Google", "Searches using Google.")
        self.google = async_cse.Search(API_KEYS, engine_id="8883d385a12302825")

    async def search(self, query: str) -> List[Result]:
        results = await self.google.search(query, safesearch=False)
        # await self.google.close()
        return [create_result(r) for r in results]
