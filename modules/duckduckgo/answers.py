from typing import List
from urllib.parse import quote

from aiohttp_requests import requests
from classes import Module, Result


class InstantAnswers(Module):
    def __init__(self):
        super().__init__("Duck answers", "Retrieve instant answers from duck duck go.")

    async def search(self, query: str) -> List[Result]:
        r = await requests.get(f"https://api.duckduckgo.com/?q={quote(query[1:-1])}&format=json&t=local_search_app")
        r = await r.json(content_type="application/x-javascript")
        summary = r["Abstract"] or r["Answer"] or r["Definition"]
        if not summary:
            return []
        image = None
        if r["Image"]:
            image = f"https://duckduckgo.com{r['Image']}"
        return [
            Result(
                title=r["Heading"],
                summary=r["Answer"] or r["Abstract"],
                uri=r["AbstractURL"] or r["DefinitionURL"],
                image=image,
                color=0xE37151,
                weight=8
            )
        ]
