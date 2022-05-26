from dataclasses import dataclass, field
from typing import Optional, List, Union
from datetime import datetime
from xml.etree import ElementTree as ET

from classes.widgets import Widget
#from utils.image import to_base64


@dataclass(
    init=True,
    repr=True,
    eq=True,
    order=True,
    unsafe_hash=True)
class Result:
    weight: int = 1
    title: str = None
    summary: Optional[str] = None
    footer: Union[None, str, datetime] = None
    color: int = 0xC51A4A
    widgets: List[Widget] = field(default_factory=list)
    uri: Optional[str] = None
    image: Union[None, str] = None

    def to_xml(self) -> ET.Element:
        root = ET.Element("result")

        root.set("title", self.title)
        root.set("summary", self.summary or "")
        root.set("color", f"#{self.color:06X}")
        root.set("weight", str(self.weight))

        if self.uri is not None:
            root.set("uri", self.uri or "")

        if isinstance(self.footer, str):
            root.set("footer", self.footer)
        elif isinstance(self.footer, datetime):
            root.set("footer", self.footer.strftime("%Y-%m-%d"))

        if self.image:
            root.set("image", self.image)

        widgets = ET.SubElement(root, "widgets")
        for widget in self.widgets:
            widgets.append(widget.to_xml())

        return root

    def to_dict(self) -> dict:
        root = dict()
        root.update({"title": self.title})
        root.update({"summary": (self.summary or "")})
        root.update({"color": f"#{self.color:06X}"})
        root.update({"weight": self.weight})

        if self.uri:
            root.update({"uri": self.uri})

        if isinstance(self.footer, str):
            root.update({"footer": self.footer})
        elif isinstance(self.footer, datetime):
            root.update({"footer": self.footer.strftime("%Y-%m-%d")})

        if self.image:
            root.update({"image": self.image})

        root["widgets"] = []
        for widget in self.widgets:
            root["widgets"].append(widget.to_dict())
        
        return root