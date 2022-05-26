from types import FunctionType
from typing import List

from utils.results import create_exception_result


async def thread_decorator(thread, func: FunctionType, add_exceptions=False, **kwargs):
    try:
        results = await thread
        if isinstance(results, BaseException) and add_exceptions:
            results = [create_exception_result(results)]
            await func(results, **kwargs)
        elif isinstance(results, List):
            await func(results, **kwargs)
    except BaseException as ex:
        if add_exceptions:
            results = [create_exception_result(ex)]
            await func(results, **kwargs)
        else:
            raise ex


def on_thread(threads, func: FunctionType, **kwargs) -> List:
    return [thread_decorator(thread, func, **kwargs) for thread in threads]
