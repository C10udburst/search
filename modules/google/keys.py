from utils.config import config

API_KEYS = {x for x in config['google']['keys'].splitlines() if x}