from xml.etree import ElementTree as ET

from classes.widgets import Widget


class Text(Widget):
    def __init__(self, message: str):
        super().__init__("text")
        self.message = message

    def content_xml(self) -> ET.Element:
        root_xml = ET.Element("content")
        root_xml.set("message", self.message)
        return root_xml

    def content_dict(self) -> dict:
        root_dict = {}
        root_dict.update({"message": self.message})
        return {"content": root_dict}

    def append_embed(self, embed):
        embed.add_field(value=self.message, name="")

    def __repr__(self):
        return f"Widget<{self.type}>({self.message})"
