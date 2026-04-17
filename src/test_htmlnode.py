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


if __name__ == "__main__":
    unittest.main()