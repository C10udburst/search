from typing import List
from urllib.parse import quote_plus

from aiohttp_requests import requests

from classes import Module, Result

from utils.config import config

APP_ID = config['wolframalpha']['app_id']


class WolframAlphaModule(Module):
    def __init__(self):
        super().__init__("Wolfram Alpha", "Query Wolfram|Alpha.")

    async def search(self, query: str) -> List[Result]:
        if not(query.replace(" ", "")[-1] == "?"
               or query.replace(" ", "")[0] == "="
               or query.replace(" ", "")[-1] == "="):
            return []

        r = await requests.get(f"https://api.wolframalpha.com/v2/query?input={quote_plus(query)}&format=image,plaintext&output=JSON&appid={APP_ID}")
        r = await r.json()
        input = None
        result = None
        image = None
        for pod in r["queryresult"]["pods"]:
            if "input" in pod["title"].lower():
                input = pod["subpods"][0]["plaintext"]
            elif "result" in pod["title"].lower():
                pod = pod["subpods"][0]
                if pod["plaintext"]:
                    result = pod["plaintext"]
                else:
                    image = pod["img"]["src"]
            elif "plot" in pod["title"].lower() and not image:
                image = pod["subpods"][0]["img"]["src"]
        footer = []
        if r["queryresult"]["success"]:
            footer.append("success")
        if r["queryresult"]["error"]:
            footer.append("error")
        footer.append(r["queryresult"]["datatypes"])
        if input or result or image:
            return [Result(
                title=input or query,
                summary=result or "",
                image=image,
                color=0xff7e00,
                weight=7,
                uri=f"https://www.wolframalpha.com/input/?i={quote_plus(query)}",
                footer=", ".join(footer)
            )]
        return []