from xml.etree import ElementTree as ET

from classes.widgets import Widget


class Field(Widget):
    def __init__(self, key: str, value: str):
        super().__init__("field")
        self.key = key
        self.value = value

    def content_xml(self) -> ET.Element:
        root_xml = ET.Element("content")
        root_xml.set("key", self.key)
        root_xml.set("value", self.value)
        return root_xml

    def content_dict(self) -> dict:
        root_dict = {}
        root_dict.update({"key": self.key, "value": self.value})
        return {"content": root_dict}

    def append_embed(self, embed):
        embed.add_field(name=self.key, value=self.value)