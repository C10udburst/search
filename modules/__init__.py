from typing import Set, List

from classes import Module
from utils.query import clean_query
from .apps import AppsModule
from .duckduckgo import duckduckgo_modules
from .files import FilesModule
from .forensics import forensics_modules
from .google import google_modules
from .help import HelpModule
from .utils import utils_modules
from .wolframalpha import WolframAlphaModule

modules: Set[Module] = set()
modules.update({
    HelpModule(modules),
    AppsModule(),
    FilesModule(),
    WolframAlphaModule(),
    *utils_modules,
    *google_modules,
    *duckduckgo_modules,
    *forensics_modules
})

print(f"Initialized {len(modules)} modules.", flush=True)


def get_threads(query: str) -> List:
    query = " " + query + " "
    threads = filter(lambda module: module.should_search(query), modules)
    cquery = clean_query(query)

    threads = [module.search(cquery) for module in threads]
    return threads
