import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><span>child2</span></div>",
        )
    
    def test_to_html_with_many_children(self):
        child_node1 = LeafNode("b", "Bold text")
        child_node2 = LeafNode(None, "Normal text")
        child_node3 = LeafNode("i", "italic text")
        child_node4 = LeafNode(None, "Normal text")
        parent_node = ParentNode("p",[child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(
            parent_node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

if __name__ == "__main__":
    unittest.main()