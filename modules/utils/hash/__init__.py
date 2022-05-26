from .hash import HashModule
from .rainbowtables import RainbowtablesModule

algorithms = ['blake2b', 'sha512_224', 'sha1', 'sha512', 'ripemd160',
              'sha224', 'sha3_384', 'shake_256', 'sha384', 'blake2s', 'sha3_512',
              'md4', 'mdc2', 'sha3_224', 'sha3_256', 'sha512_256', 'sha256', 'whirlpool',
              'sm3', 'md5', 'shake_128', 'md5-sha1']

hash_modules = {HashModule(algo) for algo in algorithms}
hash_modules = {*hash_modules, RainbowtablesModule()}