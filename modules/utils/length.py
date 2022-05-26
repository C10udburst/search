from typing import List

from classes import KeywordModule, Result
from classes.widgets import Field


class LengthModule(KeywordModule):
    def __init__(self):
        super().__init__("Length", "Get length of a string.", keywords=["len", "length"])

    async def whitelisted_search(self, query: str) -> List[Result]:
        return [Result(
            title="String length",
            widgets=[
                Field(
                    key="Length",
                    value=f"`{len(query)}`"
                )
            ],
            weight=10
        )]
