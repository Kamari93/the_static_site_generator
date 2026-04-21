import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):

    # ---------- IMAGE TESTS ----------

    def test_split_images_basic(self):
        node = TextNode(
            "Text ![img](url) end",
            TextType.TEXT
        )
        result = split_nodes_image([node])

        expected = [
            TextNode("Text ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "url"),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_images_multiple(self):
        node = TextNode(
            "A ![img1](url1) B ![img2](url2) C",
            TextType.TEXT
        )
        result = split_nodes_image([node])

        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "url1"),
            TextNode(" B ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "url2"),
            TextNode(" C", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_images_leading(self):
        node = TextNode(
            "![img](url) start",
            TextType.TEXT
        )
        result = split_nodes_image([node])

        expected = [
            TextNode("img", TextType.IMAGE, "url"),
            TextNode(" start", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_images_trailing(self):
        node = TextNode(
            "end ![img](url)",
            TextType.TEXT
        )
        result = split_nodes_image([node])

        expected = [
            TextNode("end ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "url"),
        ]
        self.assertEqual(result, expected)

    def test_split_images_no_images(self):
        node = TextNode("just text", TextType.TEXT)
        result = split_nodes_image([node])

        self.assertEqual(result, [node])

    # ---------- LINK TESTS ----------

    def test_split_links_basic(self):
        node = TextNode(
            "Text [link](url) end",
            TextType.TEXT
        )
        result = split_nodes_link([node])

        expected = [
            TextNode("Text ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url"),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_links_multiple(self):
        node = TextNode(
            "A [l1](u1) B [l2](u2) C",
            TextType.TEXT
        )
        result = split_nodes_link([node])

        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("l1", TextType.LINK, "u1"),
            TextNode(" B ", TextType.TEXT),
            TextNode("l2", TextType.LINK, "u2"),
            TextNode(" C", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_links_leading(self):
        node = TextNode(
            "[link](url) start",
            TextType.TEXT
        )
        result = split_nodes_link([node])

        expected = [
            TextNode("link", TextType.LINK, "url"),
            TextNode(" start", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_links_trailing(self):
        node = TextNode(
            "end [link](url)",
            TextType.TEXT
        )
        result = split_nodes_link([node])

        expected = [
            TextNode("end ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertEqual(result, expected)

    def test_split_links_no_links(self):
        node = TextNode("just text", TextType.TEXT)
        result = split_nodes_link([node])

        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()