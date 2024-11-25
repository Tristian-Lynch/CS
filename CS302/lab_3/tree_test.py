# vim: set tw=79 tb=4 sw=4 et
"""Tests for the generic tree used in CS302 Lab 3.

Test cases for the tree methods from tree.py

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 23, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

import unittest

from node import Node
from tree import Tree
from tree_builder import build_tree_from_json


class TreeSizeTest(unittest.TestCase):
    def test_size_no_nodes(self):
        t = Tree(3, "no_nodes_tree")
        self.assertEqual(0, t.get_size())

    def test_size_one_node(self):
        t = Tree(4, "only_root_tree", Node(4, 0))
        self.assertEqual(1, t.get_size())

    def test_size_with_add_node(self):
        root = Node(1, 0)
        t = Tree(1, "linked_list_tree", root)
        t.add_node(root, 2)
        self.assertEqual(2, t.get_size())

    def test_size_with_two_nodes(self):
        root = Node(2, 0)
        t = Tree(2, "three_nodes_tree", root)
        t.add_node(root, 2)
        t.add_node(root, 3)
        self.assertEqual(3, t.get_size())

    def test_size_with_deeper_nodes(self):
        root = Node(1, 0)
        t = Tree(1, "linked_list_tree", root)
        node = t.add_node(root, 2)
        t.add_node(node, 3)
        self.assertEqual(3, t.get_size())

    def test_size_long_linked_list(self):
        root = Node(1, 0)
        t = Tree(1, "long_linked_list_tree", root)
        # add 10 node deep into the chain
        node = root
        for i in range(10):
            node = t.add_node(node, i)
        self.assertEqual(11, t.get_size())

    def test_size_large_tree(self):
        test_file = "trees/tree_h7.json"
        t = build_tree_from_json(test_file)
        self.assertEqual(97, t.get_size())


class TreeHeightTest(unittest.TestCase):
    def test_height_empty_tree(self):
        t = Tree(10, "empty_tree")
        self.assertEqual(t.get_height(), -1)

    def test_height_single_node_tree(self):
        t = Tree(10, "only_root_tree", Node(10, 1))
        self.assertEqual(0, t.get_height())

    def test_height_node_tree(self):
        arity = 10
        t = Tree(arity, "only_root_tree", Node(arity, 1))
        self.assertEqual(t.root.height(), t.get_height())

    def test_height_two_nodes(self):
        arity = 3
        root = Node(arity, 1)
        t = Tree(arity, "two_nodes_tree", root)
        t.add_node(root, 3)
        self.assertEqual(1, t.get_height())

    def test_height_not_affected_by_going_horiz(self):
        arity = 3
        root = Node(arity, 1)
        t = Tree(arity, "four_nodes_tree", root)
        t.add_node(root, 3)
        t.add_node(root, 4)
        t.add_node(root, 5)
        self.assertEqual(4, t.get_size())
        self.assertEqual(1, t.get_height())

    def test_height_with_deeper_nodes(self):
        arity = 1
        root = Node(arity, 0)
        t = Tree(arity, "long_linked_list_tree", root)
        # add 10 node deep into the chain
        node = root
        for i in range(10):
            node = t.add_node(node, i)
        self.assertEqual(10, t.get_height())

    def test_height_large_tree(self):
        test_file = "trees/tree_h7.json"
        t = build_tree_from_json(test_file)
        self.assertEqual(7, t.get_height())


if __name__ == "__main__":
    unittest.main(verbosity=2)
