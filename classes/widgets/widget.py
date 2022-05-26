from abc import ABC, abstractmethod
from xml.etree import ElementTree as ET


class Widget(ABC):

    def __init__(self, type: str = "none"):
        self.type = type

    def to_xml(self) -> ET.Element:
        root_xml = ET.Element("widget")
        root_xml.set("type", self.type)
        root_xml.append(self.content_xml())
        return root_xml

    def to_dict(self) -> dict:
        root_dict = {}
        root_dict.update({"type": self.type})
        root_dict.update(self.content_dict())
        return {"widget": root_dict}

    @abstractmethod
    def content_xml(self) -> ET.Element:
        pass

    @abstractmethod
    def content_dict(self) -> dict:
        pass

    @abstractmethod
    def append_embed(self, embed):
        pass

    def __repr__(self):
        return f"Widget<{self.type}>"
