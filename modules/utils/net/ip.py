from typing import List

import aiohttp
from aiohttp_requests import requests
import socket
from classes import Result, KeywordModule
from classes.widgets import Field, DynamicField


class IpAddresses(KeywordModule):
    def __init__(self):
        super().__init__("IP", "Gets ip addresses.", [
            "ip",
            "ipv4",
            "ipv6"
        ])

    async def whitelisted_search(self, query: str) -> List[Result]:
        public = "0.0.0.0"
        try:
            public = await requests.get("https://api.my-ip.io/ip")
            public = await public.text()
        except aiohttp.ClientError:
            pass
        private = "0.0.0.0"
        try:
            private = socket.gethostbyname(socket.gethostname())
        except OSError:
            pass
        return [Result(
            title="IP Addresses",
            widgets=[
                Field("Public", f"`{public}`"),
                Field("Private", f"`{private}`"),
		DynamicField("Hostname", js="() => { return `\\`${window.location.hostname}\\`` }")
            ],
            weight=10
        )]
