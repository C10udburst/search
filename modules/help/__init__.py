from typing import List

from classes import KeywordModule, Result, Module
from classes.widgets import UriField, Field
from re import sub

from modules.google import GoogleCSEModule
from modules.utils.hash import HashModule


class HelpModule(KeywordModule):
    def __init__(self, modules: set):
        super().__init__("Help", "Search through modules.", keywords=[
            "help",
            "module",
            "modules",
            "features"
        ])
        self.modules = modules

    @staticmethod
    def module_filter(query: str, module: Module) -> bool:
        if module.id.lower() in query.lower():
            return True
        if module.name.lower() in query.lower():
            return True
        if isinstance(module, KeywordModule):
            for keyword in module.keywords:
                if keyword in query.lower():
                    return True
        return False

    @staticmethod
    def format_cse(engine_id: str):
        return UriField(
                key="CSE engine",
                name=engine_id,
                uri=f"https://cse.google.com/cse?cx={engine_id}"
            )

    def format_module(self, module: Module) -> Result:
        result = Result(
            title=module.name,
            summary=module.summary,
            footer=module.id,
            color=0xb7ecea,
            weight=9
        )

        if isinstance(module, GoogleCSEModule):
            result.title += " (GoogleCSEModule)"
            result.widgets.extend([self.format_cse(engine) for engine in module.engines])
        elif isinstance(module, KeywordModule):
            result.title += " (KeywordModule)"
        else:
            result.title += " (Module)"

        if isinstance(module, KeywordModule):
            keywords = [k[1:-1] for k in module.keywords]
            keywords = ", ".join(keywords)
            result.widgets.append(Field(
                key="Keywords",
                value=f"`{keywords}`"
            ))
        return result

    async def whitelisted_search(self, query: str) -> List[Result]:
        if not sub("\\s", "", query):
            return [self.format_module(module) for module in self.modules]
        return [self.format_module(module)
                for module in
                (filter(lambda mod: self.module_filter(query, mod), self.modules))]
