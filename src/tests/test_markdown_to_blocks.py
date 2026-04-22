import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_empty_string(self):
            md = ""
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])
        
        def test_markdown_to_blocks_no_double_newlines(self):
            md = "This is a single paragraph with no double newlines."
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, ["This is a single paragraph with no double newlines."])
        
        def test_markdown_to_blocks_multiple_double_newlines(self):
            md = "First paragraph.\n\n\n\nSecond paragraph with extra newlines.\n\n\nThird paragraph."
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, ["First paragraph.", "Second paragraph with extra newlines.", "Third paragraph."])



if __name__ == "__main__":
    unittest.main()