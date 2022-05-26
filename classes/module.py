from abc import ABC, abstractmethod
from typing import List
from .result import Result
from re import sub


def create_id(name: str) -> str:
    new_id = name.lower()
    new_id = sub("[\\s._-]+", "_", new_id)
    return new_id


class Module(ABC):
    def __init__(self, name: str, summary: str = ""):
        self.name = name
        self.id = create_id(self.name)
        self.summary = summary

    def __hash__(self):
        return hash((self.id, self.summary))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return self.id.__lt__(other.id)

    def __repr__(self):
        return f"Module<{self.id}>"

    def should_search(self, query) -> bool:
        if f" !{self.id} " in query:
            return False
        return True

    @abstractmethod
    async def search(self, query: str) -> List[Result]:
        pass


class KeywordModule(Module, ABC):
    def __init__(self, name: str, summary: str = "", keywords: List[str] = []):
        super().__init__(name, summary)
        self.keywords = list(set([f" {keyword.lower()} " for keyword in keywords]))

    async def search(self, query: str) -> List[Result]:
        query = query.lower()
        for keyword in self.keywords:
            if keyword in query:
                q = query.replace(keyword, "")
                try:
                    if q[-1] == " ":
                        q = q[:-1]
                    if q[-1] == " ":
                        q = q[:-1]
                except IndexError:
                    pass
                return await self.whitelisted_search(q)

    def __repr__(self):
        keywords = ",".join([k[1:-1] for k in self.keywords])
        return f"Keyword<{keywords}>"

    @abstractmethod
    async def whitelisted_search(self, query: str) -> List[Result]:
        pass
