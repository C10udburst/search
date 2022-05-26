INTERFACES = {}

try:
    from .discord import run_discord
    INTERFACES['discord'] = run_discord
except ImportError as ex:
    print(f"{ex}. Skipping adding discord interface")

try:
    from .websocket import run_websocket
    INTERFACES['websocket'] = run_websocket
except ImportError as ex:
    print(f"{ex}. Skipping adding websocket interface")

try:
    from .term import run_term
    INTERFACES['term'] = run_term
except ImportError as ex:
    print(f"{ex}. Skipping adding term interface")
