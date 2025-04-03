import unittest
from htmlcode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        # Test with no props
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), None)
        
    def test_props_to_html_one_prop(self):
        # Test with one prop
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple props
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        # The order of attributes in a dictionary isn't guaranteed,
        # so we'll check for both possible orders
        result = node.props_to_html()
        self.assertTrue(
            result == ' href="https://www.google.com" target="_blank"' or
            result == ' target="_blank" href="https://www.google.com"'
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_valueerror(self):
        with self.assertRaises(ValueError):
            LeafNode("b", None)

if __name__ == "__main__":
    unittest.main()