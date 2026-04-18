import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    # These tests creates two TextNode objects with the same properties and asserts that they are equal.
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.LINK, "https://midnightorganic.com/")
        node2 = TextNode("This is a text node", TextType.LINK, "https://midnightorganic.com/")
        self.assertEqual(node, node2)
    
    def test_eq_3(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    # These tests creates two TextNode objects with the same properties and asserts that they are not equal.
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_3(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK, "https://midnightorganic.com/")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_4(self):
        node = TextNode("Keep going", TextType.CODE, "https://midnightorganic.com/")
        node2 = TextNode("This is a text node", TextType.CODE, "https://midnightorganic.com/")
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_code_text(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})
    
    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev/image.png", "alt": "This is a text node"})
    
    def test_invalid_text_type(self):
        node = TextNode("This is a text node", "invalid_type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
            
if __name__ == "__main__":
    unittest.main()
