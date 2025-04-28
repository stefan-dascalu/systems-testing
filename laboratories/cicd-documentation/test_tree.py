import unittest
from tree import Tree
from node import Node

class TestTree(unittest.TestCase):
    def setUp(self):
        """ Setup pentru fiecare test """
        self.tree = Tree()
        for value in [10, 5, 15, 3, 7, 12, 17]:
            self.tree.add(value)

    def test_find_existing_node(self):
        """ Test pentru găsirea unui nod existent """
        node = self.tree.find(7)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 7)

    def test_find_nonexistent_node(self):
        """ Test pentru căutarea unui nod inexistent """
        node = self.tree.find(100)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
