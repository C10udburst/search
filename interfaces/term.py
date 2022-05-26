import asyncio
from modules import get_threads
from utils.results import collect_results, result_xml


async def get_results(threads) -> list:
    results = await asyncio.gather(*threads, return_exceptions=True)
    results = collect_results(results, True)
    return results


def run_term():
    query = input("> ")
    results = asyncio.run(get_results(get_threads(query)))
    for result in results:
        print(result)
