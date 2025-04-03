import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        good_node1 = TextNode("This is a text node", TextType.BOLD)
        good_node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(good_node1, good_node2)

        good_node3 = TextNode("This is a text node", TextType.ITALIC)
        good_node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(good_node3, good_node4)

        good_node5 = TextNode("This is a text node", TextType.TEXT)
        good_node6 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(good_node5, good_node6)

        dif_node1= TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        dif_node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(dif_node1, dif_node2)



if __name__ == "__main__":
    unittest.main()