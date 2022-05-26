from typing import List
from user_agent import generate_user_agent

from classes import KeywordModule, Result
from classes.widgets import Field, DynamicField


class UserAgentModule(KeywordModule):
    def __init__(self):
        super().__init__("UserAgent", "Returns your and random useragent.", [
            "ua",
            "useragent",
            "user agent",
            "brand"
        ])

    async def whitelisted_search(self, query: str) -> List[Result]:
        return [Result(
            title="User agent",
            widgets=[
                DynamicField(
                    key="Current",
                    js="() => { return `\\`${navigator.userAgent}\\`` }"
                ),
                Field(
                    key="Random",
                    value=f"`{generate_user_agent()}`"
                )
            ],
            weight=10
        )]
