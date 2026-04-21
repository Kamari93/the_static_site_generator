import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    # 1. No delimiter → unchanged
    def test_no_delimiter(self):
        node = TextNode("hello world", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result, [TextNode("hello world", TextType.TEXT)])

    # 2. Single delimiter pair
    def test_single_code_split(self):
        node = TextNode("hello `code` world", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" world", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    # 3. Multiple delimiter pairs
    def test_multiple_code_splits(self):
        node = TextNode("a `b` c `d` e", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("b", TextType.CODE),
            TextNode(" c ", TextType.TEXT),
            TextNode("d", TextType.CODE),
            TextNode(" e", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    # 4. Leading delimiter
    def test_leading_delimiter(self):
        node = TextNode("`code` world", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("code", TextType.CODE),
            TextNode(" world", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    # 5. Trailing delimiter
    def test_trailing_delimiter(self):
        node = TextNode("hello `code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    # 6. Invalid markdown (missing closing delimiter)
    def test_invalid_unclosed_delimiter(self):
        node = TextNode("hello `code world", TextType.TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    # 7. Non-TEXT nodes should be preserved
    def test_non_text_nodes_preserved(self):
        node = TextNode("bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result, [node])

    # 8. Empty string input
    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result, [])

    # 9. Mixed nodes (TEXT + already processed nodes)
    def test_mixed_nodes(self):
        nodes = [
            TextNode("hello `code`", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]

        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("bold", TextType.BOLD),
        ]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
