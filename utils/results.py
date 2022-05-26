from typing import Tuple, Union, List
from xml.etree import ElementTree as ET
from classes import Result
from json import dumps


def create_exception_result(ex: BaseException) -> Result:
    return Result(
        title=repr(ex),
        summary=str(ex.__doc__),
        color=0xFF0000,
        weight=-2
    )


def collect_results(results: Tuple[Union[List[Result], BaseException]], add_exceptions=False) -> List[Result]:
    new_results = []
    for result in results:
        if isinstance(result, BaseException):
            if add_exceptions:
                new_results.append(create_exception_result(result))
        elif isinstance(result, List):
            new_results.extend(result)
    new_results.sort()
    return new_results


def result_xml(result: Result) -> str:
    return ET.tostring(result.to_xml()).decode('utf-8')


def result_json(result: Result) -> str:
    return dumps(result.to_dict())
