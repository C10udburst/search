from typing import List, Optional
import re
import asyncio

from classes import Module, Result


class ServiceModule(Module):
    def __init__(self):
        super().__init__("Service", "Display info about services running.")

    @staticmethod
    async def service_info(name) -> Optional[Result]:
        process = await asyncio.create_subprocess_exec(
            "systemctl", "status", name, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL
        )
        stdout, stderr = await process.communicate()
        if process.returncode == 4:
            return None
        return Result(
            title=name,
            summary=f"```{stdout.decode().strip()}```",
            color=0x30D475,
            weight=2
        )

    async def search(self, query: str) -> List[Result]:
        services = re.findall("[a-z0-9]+\\.service", query)
        if len(services) < 1:
            return []
        results = await asyncio.gather(*map(self.service_info, services), return_exceptions=True)
        results = list(filter(lambda x: isinstance(x, Result), results))
        return results
