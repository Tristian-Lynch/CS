# vim: set tw=79 tb=4 sw=4 et
"""Tests for the generic tree used in CS302 Lab 3.

Test cases for the tree methods from tree.py

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 23, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

from binary_tree import BinaryTree
from binary_node import BinaryNode
from tree_builder import build_tree_from_json
import unittest


class BinaryTreeContainsTest(unittest.TestCase):
    """This class includes tests for the contains method of a BinaryTree."""

    def test_contains_empty_tree(self):
        bt = BinaryTree("empty_tree")
        # try a few values, they should all fail.
        self.assertFalse(bt.contains(5))
        self.assertFalse(bt.contains(10))
        self.assertFalse(bt.contains(-1))

    def test_contains_only_root(self):
        bt = BinaryTree("root_only_tree", BinaryNode(3))
        self.assertTrue(bt.contains(3))
        self.assertFalse(bt.contains(5))
        self.assertFalse(bt.contains(0))

    def test_contains_linked_list(self):
        bt = BinaryTree("small_list_tree", BinaryNode(3))
        bt.root.left = BinaryNode(10)
        bt.root.left.left = BinaryNode(5)

        # Should contain 3, 10, and 5
        self.assertTrue(bt.contains(5))
        self.assertTrue(bt.contains(3))
        self.assertTrue(bt.contains(10))

        # try a few values other than those.
        self.assertFalse(bt.contains(-1))
        self.assertFalse(bt.contains(100))
        self.assertFalse(bt.contains(0))

    def test_contains_degenerate_tree(self):
        root = BinaryNode(-1)
        bt = BinaryTree("degenerate_tree", root)
        node = root
        for i in range(10):
            node.right = BinaryNode(i)
            node = node.right

        # shold find -1, 0, 1, ..., 9
        for i in range(-1, 10, 1):
            self.assertTrue(bt.contains(i))

        # try a few failing ones.
        self.assertFalse(bt.contains(-2))
        self.assertFalse(bt.contains(11))
        self.assertFalse(bt.contains(100))

    def test_contains_small_tree(self):
        tree_file = 'trees/binary_tree.json'
        bt = build_tree_from_json(tree_file)

        # try to find a few.
        self.assertTrue(bt.contains(2))
        self.assertTrue(bt.contains(5))
        self.assertTrue(bt.contains(13))
        self.assertTrue(bt.contains(8))

        # try a few that fail
        self.assertFalse(bt.contains(-1))
        self.assertFalse(bt.contains(20))
        self.assertFalse(bt.contains(-100))

    def test_contains_large_tree(self):
        tree_file = 'trees/tree_h7.json'
        bt = build_tree_from_json(tree_file)

        # try to find a few.
        self.assertTrue(bt.contains(63))
        self.assertTrue(bt.contains(131))
        self.assertTrue(bt.contains(83))
        self.assertTrue(bt.contains(174))

        # try a few that fail
        self.assertFalse(bt.contains(-1))
        self.assertFalse(bt.contains(256))
        self.assertFalse(bt.contains(-100))


class BinaryTreeSearchPropertyTest(unittest.TestCase):
    def test_search_property_empty_tree(self):
        bst = BinaryTree("empty_tree")
        self.assertTrue(bst.has_search_property())

    def test_search_property_only_root(self):
        bst = BinaryTree("root_only_tree", BinaryNode(3))
        self.assertTrue(bst.has_search_property())

    def test_search_property_linked_list(self):
        bst = BinaryTree("small_list_tree", BinaryNode(3))
        bst.root.left = BinaryNode(2)
        bst.root.left.left = BinaryNode(1)
        self.assertTrue(bst.has_search_property())

    def test_search_property_bad_linked_list(self):
        bst = BinaryTree("small_list_tree", BinaryNode(3))
        bst.root.left = BinaryNode(2)
        bst.root.left.left = BinaryNode(4)
        self.assertFalse(bst.has_search_property())

    def test_search_property_degenerate_tree(self):
        root = BinaryNode(-1)
        bst = BinaryTree("degenerate_tree", root)
        node = root
        for i in range(10):
            node.right = BinaryNode(i)
            node = node.right
        self.assertTrue(bst.has_search_property())

    def test_search_property_bad_degenerate_tree(self):
        root = BinaryNode(-1)
        bst = BinaryTree("degenerate_tree", root)
        node = root
        for i in range(10):
            node.right = BinaryNode(i)
            node = node.right
        node.right = BinaryNode(-2)
        self.assertFalse(bst.has_search_property())

    def test_search_property_small_tree(self):
        json_file = 'trees/bst_10_nodes.json'
        bst = build_tree_from_json(json_file)
        self.assertTrue(bst.has_search_property())

    def test_search_property_modified_small_tree(self):
        json_file = 'trees/tree_10_nodes.json'
        bst = build_tree_from_json(json_file)
        self.assertFalse(bst.has_search_property())

    def test_search_property_another_modified_small_tree(self):
        json_file = 'trees/bst_test_3.json'
        bst = build_tree_from_json(json_file)
        self.assertFalse(bst.has_search_property())

    def test_search_property_more_modified_small_tree(self):
        json_file = 'trees/bst_test_4.json'
        bst = build_tree_from_json(json_file)
        self.assertFalse(bst.has_search_property())

    def test_search_property_large_tree(self):
        json_file = 'trees/large_bst.json'
        bst = build_tree_from_json(json_file)
        self.assertTrue(bst.has_search_property())


if __name__ == '__main__':
    unittest.main(verbosity=2)