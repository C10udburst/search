from types import FunctionType
from xml.etree import ElementTree as ET

from classes.widgets import Widget

default_js = "() => { return \"-\" }"


def default_py():
    return "-"


class DynamicField(Widget):
    def __init__(self, key: str, interval: int = -1, js: str = default_js, python: FunctionType = default_py):
        super().__init__("dynamic_field")
        self.key = key
        self.interval = interval
        self.js = js
        self.python = python

    def content_xml(self) -> ET.Element:
        root_xml = ET.Element("content")
        root_xml.set("key", self.key)
        root_xml.set("js", self.js)
        root_xml.set("value", self.python())
        root_xml.set("interval", str(self.interval))
        return root_xml

    def content_dict(self) -> dict:
        root_dict = {}
        root_dict.update({
            "key": self.key,
            "value": self.python(),
            "js": self.js,
            "interval": self.interval
        })
        return {"content": root_dict}

    def append_embed(self, embed):
        embed.add_field(name=self.key, value=self.python())
