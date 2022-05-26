from sys import argv

from interfaces import INTERFACES


for interface in argv[1:]:
    try:
        INTERFACES[interface]()
    except Exception as ex:
        print(f"Couldn't start {interface}: {ex}")
