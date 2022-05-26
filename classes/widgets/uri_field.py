from xml.etree import ElementTree as ET

from classes.widgets import Widget


class UriField(Widget):
    def __init__(self, key: str, name: str, uri: str):
        super().__init__("uri_field")
        self.key = key
        self.name = name
        self.uri = uri

    def content_xml(self) -> ET.Element:
        root_xml = ET.Element("content")
        root_xml.set("key", self.key)
        root_xml.set("name", self.name)
        root_xml.set("uri", self.uri)
        return root_xml

    def content_dict(self) -> dict:
        root_dict = {}
        root_dict.update({
            "key": self.key,
            "name": self.name,
            "uri": self.uri
        })
        return {"content": root_dict}

    def append_embed(self, embed):
        uri = self.uri
        if uri.startswith("/"):
            uri = "https://192.168.1.15"+uri
        embed.add_field(name=self.key, value=f"[{self.name}]({uri})")
