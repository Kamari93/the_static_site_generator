import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", None, None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode("a", None, None, {})
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_none(self):
        node = HTMLNode("a", None, None, None)
        self.assertEqual(node.props_to_html(), '')
    
    def test_repr(self):
        node = HTMLNode("a", None, None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode(a, None, None, {'href': 'https://www.boot.dev', 'target': '_blank'})")
    
    def test_to_html_not_implemented(self):
        node = HTMLNode("a", None, None, {"href": "https://www.boot.dev", "target": "_blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_to_html_with_children(self):
        child1 = HTMLNode("span", None, None, {"class": "child"})
        child2 = HTMLNode("span", None, None, {"class": "child"})
        parent = HTMLNode("div", [child1, child2], None, {"class": "parent"})

        with self.assertRaises(NotImplementedError):
            parent.to_html()
    
    def test_to_html_with_text(self):
        node = HTMLNode("p", None, "This is a paragraph.", {"class": "text"})
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_to_html_with_children_no_error(self):
        child1 = HTMLNode("span", None, None, {"class": "child"})
        child2 = HTMLNode("span", None, None, {"class": "child"})
        parent = HTMLNode("div", [child1, child2], None, {"class": "parent"})

        with self.assertRaises(NotImplementedError):
            parent.to_html()


if __name__ == "__main__":
    unittest.main()