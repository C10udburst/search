from typing import List
import re
from urllib.parse import quote

from classes import Module, Result


class RegexModule(Module):
    def __init__(self):
        super().__init__("Regex", "Displays regex visualization.")

    @staticmethod
    def valid_regex(regex):
        try:
            re.compile(regex)
        except re.error:
            return False
        return True

    async def search(self, query: str) -> List[Result]:
        regex = re.findall("/.+/", query)
        if not regex:
            return []
        regex = regex[0][1:-1]
        if not self.valid_regex(regex):
            return []
        return [Result(
            title="Regex",
            summary=f'<iframe frameborder="0"src="https://jex.im/regulex/#!embed=true&flags=&re={quote(regex)}"></iframe>',
            color=0x40C0FF,
            weight=9
        )]