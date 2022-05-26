from re import compile

module_blacklist = compile("![a-z0-9_]+")
exception_pattern = compile("\\s\\+((err(or)?)|(ex[ception]{0,7}))\\s")


def clean_query(query: str) -> str:
    query = module_blacklist.sub(" ", query)
    query = exception_pattern.sub(" ", query)
    return query
