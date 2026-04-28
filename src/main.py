import os
import sys
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from copy_static import copy_static_to_public
from generate_page import generate_page, generate_pages_recursive


def main():
    # print("hello world")
    # text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(repr(text_node))
    # htmlnode = HTMLNode("a", None, None, {"href": "https://www.boot.dev", "target": "_blank",})
    # print(repr(htmlnode))
    # leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(repr(leafnode))
    # parent_node = ParentNode("div", [leafnode], {"class": "container"})
    # print(repr(parent_node))

    print("keep going...")
    # basepath for github pages
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(base_dir, "static")
    public_dir = os.path.join(base_dir, "public")
    
    # content_path = os.path.join(base_dir, "content", "index.md")
    content_path = os.path.join(base_dir, "content")
    template_path = os.path.join(base_dir,"template.html")
    # dest_path = os.path.join(base_dir, "public", "index.html")

    # 1. Copy static files
    copy_static_to_public(static_dir, public_dir)
    
    # 2. Generate page(s)
    # generate_page(content_path, template_path, dest_path)
    generate_pages_recursive(content_path, template_path, public_dir, basepath)


if __name__ == "__main__":
    main()