from .base64 import base64_modules
from .regex import RegexModule
from .net import net_utils
from .hash import hash_modules
from .system import system_modules
from .length import LengthModule

utils_modules = {
    RegexModule(),
    LengthModule(),
    *base64_modules,
    *net_utils,
    *hash_modules,
    *system_modules
}
