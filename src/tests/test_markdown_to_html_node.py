import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from markdown_to_html_node import markdown_to_html_node
from textnode import TextNode
class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    
    
    def test_paragraphsII(self):
        md = """
This is **bolded** text
in a paragraph

This is another paragraph with _italic_ text
"""
        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> text in a paragraph</p>"
            "<p>This is another paragraph with <i>italic</i> text</p></div>"
        )


    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    def test_heading(self):
        md = "# Hello world"
        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><h1>Hello world</h1></div>"
        )

    def test_code_block(self):
        md = """
```
print('hello')
print('world')
```
"""

        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><pre><code>print('hello')\nprint('world')</code></pre></div>"
        )

    def test_quote_block(self):
        md = """
> This is a quote
> spread over lines
"""

        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is a quote spread over lines</blockquote></div>"
        )
    
    def test_heading_levels(self):
        md = """
# Title one

## Title two

### Title three
"""
        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><h1>Title one</h1><h2>Title two</h2><h3>Title three</h3></div>"
        )

    def test_unordered_list(self):
        md = """
- item one
- item two
- item three
"""
        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><ul><li>item one</li><li>item two</li><li>item three</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. first
2. second
3. third
"""
        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><ol><li>first</li><li>second</li><li>third</li></ol></div>"
        )

    def test_quote_block(self):
        md = """
> line one
> line two
> line three
"""
        html = markdown_to_html_node(md).to_html()

        self.assertEqual(
            html,
            "<div><blockquote>line one line two line three</blockquote></div>"
        )

if __name__ == "__main__":
    unittest.main()
