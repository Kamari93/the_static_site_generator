import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_basic_title(self):
        md = "# Hello World"
        self.assertEqual(extract_title(md), "Hello World")

    def test_title_with_content_below(self):
        md = """# My Title

This is a paragraph.

## Subtitle
"""
        self.assertEqual(extract_title(md), "My Title")

    def test_ignores_non_h1(self):
        md = """## Not the title
### Still not
# Actual Title
"""
        self.assertEqual(extract_title(md), "Actual Title")

    def test_no_h1_raises(self):
        md = """## Subtitle
No h1 here
"""
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()