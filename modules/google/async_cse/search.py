"""
MIT License

Copyright (c) 2018-2020 crrapi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
import random
from typing import Union
from urllib.parse import quote

import aiohttp

log = logging.getLogger(__name__)


class CSEBaseException(Exception):
    """Base class for all async_cse Exceptions."""


class NoResults(CSEBaseException):
    """Query yielded no results."""


class APIError(CSEBaseException):
    """Internal API error."""


class NoMoreRequests(CSEBaseException):
    """Out of requests for today."""


class Result:
    """
    Represents a result from a search query.
    You do not make these on your own, you usually get them from async_cse.Search.search.
    """

    def __init__(self, title, description, url, image_url):
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url

    def __str__(self):
        return "<async_cse.search.Result object, url: {}, image_url: {}>".format(
            self.url, self.image_url
        )

    def __repr__(self):
        return "<async_cse.search.Result object, url: {}, image_url: {}>".format(
            self.url, self.image_url
        )

    @classmethod
    def from_raw(cls, data, img):
        """Converts a dict to Result objects"""
        results = list()
        for item in data["items"]:
            title = item.get("title")
            desc = item.get("snippet")
            if img:
                image_url = item["link"]
                try:
                    url = item["image"]["contextLink"]
                except KeyError:
                    url = image_url
            else:
                url = item["link"]
                i = item.get("pagemap")
                if not i:
                    image_url = None # GOOGLE_FAVICON
                else:
                    img_a = i.get("cse_image")
                    if not i:
                        image_url = None # GOOGLE_FAVICON
                    else:
                        try:
                            image_url = img_a[0]["src"]
                            if image_url.startswith("x-raw-image"):
                                image_url = i["cse_thumbnail"][0]["src"]
                        except TypeError:
                            image_url = None # GOOGLE_FAVICON
            results.append(cls(title, desc, url, image_url))
        return results


class Search:
    """Client for custom searches."""

    def __init__(
        self,
        api_keys: Union[str, list, set],
        engine_id: str = "015786823554162166929:mywctwj8es4",
        image_engine_id: str = "015786823554162166929:szgrbbrrox0",
        session: aiohttp.ClientSession = None,
    ):
        """You may provide a list of API keys and async-cse will shuffle between them."""
        self.shuffle = False
        if isinstance(api_keys, set):
            api_keys = list(api_keys)
        if isinstance(api_keys, list):
            self.shuffle = True
        self.api_keys = api_keys  # API keys for the CSE API
        self.engine_id = engine_id
        self.image_engine_id = image_engine_id
        self.search_url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&safe={}"  # URL for requests
        self.session = session or None
        self.log = log

    def __repr__(self):
        return "<async_cse Search object, engine id: {}>".format(self.engine_id)

    def __str__(self):
        return "<async_cse Search object, engine id: {}>".format(self.engine_id)

    async def close(self):
        """Properly close the client."""
        if self.session:
            await self.session.close()

    async def search(self, query: str, *, safesearch=True, image_search=False):
        """Searches Google for a given query."""
        while self.api_keys:
            key = self.api_keys if not self.shuffle else random.choice(self.api_keys)
            resp = await self._do_search(
                query, key, safesearch=safesearch, image_search=image_search
            )
            error = resp.get("error")
            if error:
                if error.get("errors")[0].get("domain") == "usageLimits":
                    if self.shuffle:
                        self.log.warning(
                            "Key {} is out of requests. I've removed it from my list.".format(
                                self.api_keys.index(key)
                            )
                        )
                        self.api_keys.remove(key)
                    else:
                        raise NoMoreRequests(
                            "[100 Request Limit] "
                            "You have to wait a day before you can make more requests. "
                            "Consider passing multiple keys in a list to avoid this."
                        )
                else:
                    raise APIError(
                        ", ".join([error["message"] for err in error["errors"]])
                    )
            elif not resp.get("items"):
                raise NoResults("Your query {} returned no results.".format(query))
            else:
                return Result.from_raw(resp, img=image_search)
        else:
            raise NoMoreRequests(
                "All the API keys you gave me are out of requests for today."
            )

    async def _do_search(
        self, query: str, key: str, *, safesearch=True, image_search=False
    ):
        """Internal function for searching."""
        if not self.session or self.session.closed:
            self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))  # Session for making requests

        if safesearch:
            safesearch = "active"
        else:
            safesearch = "off"
        if image_search:
            image_search = "image"

        url = self.search_url.format(
            key,
            self.image_engine_id if image_search else self.engine_id,
            quote(query),
            safesearch,
        )
        if image_search:
            url += "&searchType=image"
        async with self.session.get(url) as resp:
            return await resp.json(content_type=None)
