from typing import Optional

from classes import Result
from . import async_cse


def create_result(from_value: async_cse.Result, weight: int = 3, color: int = 0x1aa260) -> Optional[Result]:
    try:
        result = Result(
            title=from_value.title,
            summary=from_value.description,
            uri=from_value.url,
            image=from_value.image_url,
            footer=from_value.url,
            weight=weight,
            color=color
        )
        return result
    except AttributeError:
        return None
