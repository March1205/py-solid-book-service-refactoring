import json
import xml.etree.ElementTree as ET
from app.book import Book


class SerializeStrategy:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError("Serialize method it not implemented yet")


class JSONSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
