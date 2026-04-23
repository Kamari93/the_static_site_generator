import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):

    # 1. Paragraph (default case)
    def test_paragraph(self):
        block = "This is just a normal paragraph."
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    # 2. Heading (valid)
    def test_heading(self):
        block = "### This is a heading"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.HEADING)

    # 3. Heading invalid (no space)
    def test_heading_no_space(self):
        block = "###Invalid heading"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    # 4. Heading invalid (too many #)
    def test_heading_too_many_hashes(self):
        block = "####### Too many hashes"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    # 5. Code block
    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.CODE)

    # 6. Quote block (multi-line)
    def test_quote_block(self):
        block = "> This is a quote\n> This is still a quote"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.QUOTE)

    # 7. Quote invalid (one line missing >)
    def test_quote_invalid(self):
        block = "> valid line\nnot a quote"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    # 8. Unordered list
    def test_unordered_list(self):
        block = "- item one\n- item two\n- item three"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.UNORDERED)

    # 9. Unordered invalid
    def test_unordered_invalid(self):
        block = "- item one\nitem two"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    # 10. Ordered list
    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.ORDERED)

    # 11. Ordered invalid (wrong sequence)
    def test_ordered_invalid_sequence(self):
        block = "1. first\n3. second\n4. third"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    # 12. Ordered invalid (doesn't start at 1)
    def test_ordered_invalid_start(self):
        block = "2. first\n3. second"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()