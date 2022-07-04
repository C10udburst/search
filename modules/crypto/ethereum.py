from typing import List
import re
from aiohttp_requests import requests
from user_agent import generate_user_agent
import asyncio

from classes import Module, Result


class EthereumModule(Module):
    def __init__(self):
        super().__init__("Ethereum", "Display info about an ethereum address.")

    async def fetch_address(self, address):
        headers = {"User-Agent": generate_user_agent()}
        data = await requests.get(f"https://api.blockchair.com/ethereum/dashboards/address/{address}", headers=headers)
        data = await data.json()
        data = data['data'][address]['address']
        summary = f"Call count: {data['call_count']}"
        if data['type'] == "account":
            summary += f"\nBalance: ${data['balance_usd']:.2f} ({data['balance']} WEI)"
        elif data['type'] == "contract":
            token_data = await requests.get(f"https://api.blockchair.com/ethereum/erc-20/{address}/stats", headers=headers)
            token_data = await token_data.json()
            token_data = token_data['data']
            summary += f"\nName: {token_data['name']}, ${token_data['symbol']}"
            summary += f"\nPrice: ${(token_data['market_price_usd'] or 0):.2f}" 
        return Result(
            title=f"{data['type'].capitalize()} on {address}",
            summary=summary,
            color=0x9AAADD
        )

    async def search(self, query: str) -> List[Result]:
        addresses = re.findall("0x[a-fA-F0-9]{40}", query)
        if not addresses:
            return []
        results = asyncio.gather(*[fetch_address(x) for x in addresses], return_exceptions=True)
        results = [result for result in results if isinstance(result, Result)]
        return results
