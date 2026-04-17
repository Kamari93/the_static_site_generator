from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        # make sure comparing compatible objects
        if not isinstance(other, TextNode):
            return NotImplemented
        # compare based on specific attributes
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        # return a string that could recreate the object
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


