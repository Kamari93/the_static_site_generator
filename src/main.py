from textnode import TextNode, TextType
from htmlnode import HTMLNode
print("hello world")

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(text_node))
    htmlnode = HTMLNode("a", None, None, {"href": "https://www.boot.dev", "target": "_blank",})
    print(repr(htmlnode))


if __name__ == "__main__":
    main()