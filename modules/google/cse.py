import asyncio
from typing import List, Union

from classes import KeywordModule, Result
from utils import flatten
from .keys import API_KEYS
from . import async_cse
from .utils import create_result


class GoogleCSEModule(KeywordModule):
    def __init__(self, name: str, engine_id: Union[str, List[str]], keywords: List[str] = [], summary: str = ""):
        super().__init__(name, summary, keywords)

        if isinstance(engine_id, str):
            engine_id = [engine_id]
        self.engines = engine_id
        self.googles = [
            async_cse.Search(API_KEYS, engine_id=engine)
            for engine in self.engines
        ]

    def __repr__(self):
        keywords = ",".join([k[1:-1] for k in self.keywords])
        return f"CSE({','.join(self.engines)})<{keywords}>"

    async def close(self):
        await asyncio.gather(*[e.close() for e in self.googles])

    async def whitelisted_search(self, query: str) -> List[Result]:
        results = await asyncio.gather(*[
            google.search(query, safesearch=False)
            for google in self.googles
        ], return_exceptions=True)
        results = flatten(results)
        # await self.close()
        return list(filter(bool, [create_result(r, weight=4, color=0xffce44) for r in results]))
