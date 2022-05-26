from typing import List
import re
from aiohttp_requests import requests
from user_agent import generate_user_agent

from classes import Module, Result

from classes.widgets import UriField


class EmailModule(Module):
    def __init__(self):
        super().__init__("Email", "Display info about an email.")

    @property
    def headers(self):
        return {
            "Vaar-Header-App-Build-Version": "1.0.0",
            "Vaar-Header-App-Product": "hackcheck-web-avast",
            "Vaar-Header-App-Product-Name": "hackcheck-web-avast",
            "Vaar-Version": "0",
            "Host": "identityprotection.avast.com",
            "Origin": "https://www.avast.com",
            "Referer": "https://www.avast.com/",
            "User-Agent": generate_user_agent()
        }

    async def search(self, query: str) -> List[Result]:
        emails = re.findall("[^@\\s]+@[^@\\s\\.]+\\.[^@\\.\\s]+", query)
        if not emails:
            return []
        data = await requests.post(
            "https://identityprotection.avast.com/v1/web/query/site-breaches/unauthorized-data",
            headers=self.headers,
            json={"emailAddresses": emails}
        )
        data = await data.json()
        results = []
        email_mappings = dict.fromkeys(emails, [])
        for breach in data["data"].keys():
            for email in data["data"][breach].keys():
                breach_data = data["data"][breach][email][0]
                email_mappings[email].append({
                    "url": breach,
                    "username": breach_data["usernameBreached"],
                    "password": breach_data["passwordBreached"]
                })
        for email in emails:
            breaches = email_mappings[email]
            if not breaches:
                continue
            result = Result(
                title=f"{email} leaks",
                summary=f"{len(breaches)} breaches found.",
                color=0xFF7800
            )
            for breach in breaches:
                field = UriField(
                    uri=f"http://{breach['url']}",
                    key=breach["url"],
                    name=f"Password: {breach['password']}, username: {breach['username']}"
                )
                result.widgets.append(field)
            results.append(result)
        return results
