import asyncio
from typing import List
from urllib.parse import quote_plus
from aiohttp_requests import requests

from classes import Result, KeywordModule
from classes.widgets import UriField
from utils.results import collect_results


async def get_aptoide(query):
    r = await requests.get(f"https://ws75-cache.aptoide.com/api/7/apps/search?query={quote_plus(query)}&limit=20")
    r = await r.json()
    results = []
    for item in r["datalist"]["list"]:
        widgets = [UriField("Main file", "Download", item["file"]["path"])]
        if item['obb'] is not None:
            for key in item['obb'].keys():
                widgets.append(UriField(
                    f"{key}.obb",
                    "Download",
                    item['obb'][key]['path']
                ))
        result = Result(
            title=item["name"],
            summary=f"{item['package']} {item['file']['malware']['rank']}",
            widgets=widgets,
            color=0xa4c639,
            image=item["icon"]
        )
        results.append(result)
    return results


class AppsModule(KeywordModule):
    def __init__(self):
        super().__init__("Apps", "Search for Android apps.", [
            "apps",
            "apk",
            "android",
            "mobile"
        ])

    async def whitelisted_search(self, query: str) -> List[Result]:
        results = await asyncio.gather(
            get_aptoide(query)
        )
        return collect_results(results)
