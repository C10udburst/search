from typing import List
from aiohttp_requests import requests

from classes import KeywordModule, Result
from classes.widgets import UriField

from utils.config import config

class FilesModule(KeywordModule):
    def __init__(self):
        super().__init__("Files", "Search for files", keywords=[
            "files",
            "file",
            "dl",
            "download"
        ])
        self.types = ["video", "audio", "ebook", "archive", "mobile"]

    def get_type(self, query: str):
        for type in self.types:
            if f" {type} " in query:
                query = query.replace(f" {type} ", "")
                return type, query
        return None, query

    @property
    def headers(self):
        return {
            'x-rapidapi-key': config['files']['filepursuit_key'],
            'x-rapidapi-host': "filepursuit.p.rapidapi.com"
        }

    @staticmethod
    def format_result(entry: dict) -> Result:
        return Result(
            title=f"{entry['file_name']} Filepursuit",
            summary=entry['readable_path'],
            footer=entry['time_ago'],
            widgets=[UriField(
                key=entry['file_name'],
                name="Download",
                uri=entry['file_link']
            )],
            weight=2,
            color=0x105880
        )

    async def whitelisted_search(self, query: str) -> List[Result]:
        type, query = self.get_type(query)
        params = {"q": query}
        if type:
            params.update({"type": type})
        r = await requests.get("https://filepursuit.p.rapidapi.com/", headers=self.headers, params=params)
        r = await r.json()
        return list(filter(bool, [self.format_result(e) for e in r["files_found"]]))
