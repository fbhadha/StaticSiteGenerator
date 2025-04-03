import unittest
from htmlcode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()