import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from textnode import TextNode, TextType
from split_nodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    # 1. Basic conversion with no markdown → single Text node
    def test_test_to_text_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)
    
        # 1. Plain text only
    def test_plain_text(self):
        text = "just some text"
        result = text_to_textnodes(text)

        expected = [TextNode("just some text", TextType.TEXT)]
        self.assertEqual(result, expected)

    # 2. Bold text
    def test_bold_text(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    # 3. Italic text
    def test_italic_text(self):
        text = "This is _italic_ text"
        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    # 4. Code text
    def test_code_text(self):
        text = "This is `code` text"
        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    # 5. Image parsing
    def test_image(self):
        text = "Here is an ![img](url)"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "url"),
        ]
        self.assertEqual(result, expected)

    # 6. Link parsing
    def test_link(self):
        text = "Click [here](url)"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "url"),
        ]
        self.assertEqual(result, expected)

    # 7. Mixed formatting (real-world case)
    def test_mixed(self):
        text = "This is **bold** and _italic_ with `code`"
        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    # 8. Full complex example (everything together)
    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi](img_url) and a [link](link_url)"
        )

        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi", TextType.IMAGE, "img_url"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "link_url"),
        ]

        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()