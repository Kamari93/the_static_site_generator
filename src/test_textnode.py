import unittest
from textnode import TextNode, TextType

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
        node = TextNode("Keep going", TextType.CODE_TEXT, "https://midnightorganic.com/")
        node2 = TextNode("This is a text node", TextType.CODE_TEXT, "https://midnightorganic.com/")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
