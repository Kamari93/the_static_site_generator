from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
print("hello world")

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(text_node))
    htmlnode = HTMLNode("a", None, None, {"href": "https://www.boot.dev", "target": "_blank",})
    print(repr(htmlnode))
    leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(repr(leafnode))
    parent_node = ParentNode("div", [leafnode], {"class": "container"})
    print(repr(parent_node))


if __name__ == "__main__":
    main()