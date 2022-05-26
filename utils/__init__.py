from collections.abc import Iterable


def flatten(t):
    t = list(filter(lambda x: isinstance(x, Iterable), t))
    return [item for sublist in t for item in sublist]