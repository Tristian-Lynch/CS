# vim: set tw=79 tb=4 sw=4 et
"""Tests for the generic tree used in CS302 Lab 3.

Test cases for the tree methods from tree.py

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 23, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

import sys
import unittest
from io import StringIO

from tree_builder import build_tree_from_json


class BinaryTreePreOrderTraversalTest(unittest.TestCase):
    """
    This class includes tests for the preorder traversal method of a
    BinaryTree.
    """

    def test_first_tree(self):
        tree_file = "trees/first_tree.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.preorder_traversal()
            self.assertEqual(capture.getvalue().rstrip(), "0 1 3 2 5 7")
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_tree_with_10_nodes(self):
        tree_file = "trees/tree_10_nodes.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.preorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "100 25 15 10 20 35 30 40 75 60 55 65 85 80 90",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_binary_tree(self):
        tree_file = "trees/binary_tree.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.preorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(), "0 1 3 7 8 4 9 10 2 5 11 12 6 13 14"
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_tree_h7(self):
        tree_file = "trees/tree_h7.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.preorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                """0 1 3 7 15 31 63 127 128 64 129 130 32 65 131 132 66 133 134 16 33 67 135 136 68 137 138 34 69 139 140 70 141 142 8 17 35 71 143 144 72 145 146 36 73 147 148 74 149 150 18 37 75 151 152 76 153 154 38 77 155 156 78 157 158 4 9 19 39 79 159 160 80 161 162 40 81 163 164 82 165 166 20 41 83 167 168 84 169 170 42 85 171 172 86 173 174""",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_bst_3(self):
        tree_file = "trees/bst_test_3.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.preorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "50 25 15 10 20 35 70 40 75 60 55 65 85 80 90",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_bst_4(self):
        tree_file = "trees/bst_test_4.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.preorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "50 25 15 10 20 35 30 40 75 60 55 65 85 30 90",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_large_bst(self):
        tree_file = "trees/large_bst.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.preorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "50 25 12 6 3 8 18 15 20 37 30 28 33 45 42 48 75 63 58 55 60 68 65 70 88 80 78 85 95 92 98",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise


class BinaryTreeInOrderTraversalTest(unittest.TestCase):
    """
    This class includes tests for the inorder traversal method of a
    BinaryTree.
    """

    def test_first_tree(self):
        tree_file = "trees/first_tree.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.inorder_traversal()
            self.assertEqual(capture.getvalue().rstrip(), "3 1 0 5 2 7")
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_tree_with_10_nodes(self):
        tree_file = "trees/tree_10_nodes.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.inorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "10 15 20 25 30 35 40 100 55 60 65 75 80 85 90",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_binary_tree(self):
        tree_file = "trees/binary_tree.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.inorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(), "7 3 8 1 9 4 10 0 11 5 12 2 13 6 14"
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_tree_h7(self):
        tree_file = "trees/tree_h7.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.inorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                """127 63 128 31 129 64 130 15 131 65 132 32 133 66 134 7 135 67 136 33 137 68 138 16 139 69 140 34 141 70 142 3 143 71 144 35 145 72 146 17 147 73 148 36 149 74 150 8 151 75 152 37 153 76 154 18 155 77 156 38 157 78 158 1 159 79 160 39 161 80 162 19 163 81 164 40 165 82 166 9 167 83 168 41 169 84 170 20 171 85 172 42 173 86 174 4 0""",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_bst_3(self):
        tree_file = "trees/bst_test_3.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.inorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "10 15 20 25 70 35 40 50 55 60 65 75 80 85 90",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_bst_4(self):
        tree_file = "trees/bst_test_4.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.inorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "10 15 20 25 30 35 40 50 55 60 65 75 30 85 90",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_large_bst(self):
        tree_file = "trees/large_bst.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.inorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "3 6 8 12 15 18 20 25 28 30 33 37 42 45 48 50 55 58 60 63 65 68 70 75 78 80 85 88 92 95 98",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise


class BinaryTreePostOrderTraversalTest(unittest.TestCase):
    """
    This class includes tests for the postorder traversal method of a
    BinaryTree.
    """

    def test_first_tree(self):
        tree_file = "trees/first_tree.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.postorder_traversal()
            self.assertEqual(capture.getvalue().rstrip(), "3 1 5 7 2 0")
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_tree_with_10_nodes(self):
        tree_file = "trees/tree_10_nodes.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.postorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "10 20 15 30 40 35 25 55 65 60 80 90 85 75 100",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_binary_tree(self):
        tree_file = "trees/binary_tree.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.postorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(), "7 8 3 9 10 4 1 11 12 5 13 14 6 2 0"
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_tree_h7(self):
        tree_file = "trees/tree_h7.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.postorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "127 128 63 129 130 64 31 131 132 65 133 134 66 32 15 135 "
                "136 67 137 138 68 33 139 140 69 141 142 70 34 16 7 143 "
                "144 71 145 146 72 35 147 148 73 149 150 74 36 17 151 "
                "152 75 153 154 76 37 155 156 77 157 158 78 38 18 8 3 "
                "159 160 79 161 162 80 39 163 164 81 165 166 82 40 19 "
                "167 168 83 169 170 84 41 171 172 85 173 174 86 42 20 9 4 1 0",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_bst_3(self):
        tree_file = "trees/bst_test_3.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.postorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "10 20 15 70 40 35 25 55 65 60 80 90 85 75 50",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_bst_4(self):
        tree_file = "trees/bst_test_4.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.postorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "10 20 15 30 40 35 25 55 65 60 30 90 85 75 50",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise

    def test_large_bst(self):
        tree_file = "trees/large_bst.json"
        bt = build_tree_from_json(tree_file)

        capture = StringIO()
        sys.stdout = capture
        try:
            bt.postorder_traversal()
            self.assertEqual(
                capture.getvalue().rstrip(),
                "3 8 6 15 20 18 12 28 33 30 42 48 45 37 25 55 "
                "60 58 65 70 68 63 78 85 80 92 98 95 88 75 50",
            )
            sys.stdout = sys.__stdout__
        except:
            sys.stdout = sys.__stdout__
            raise


if __name__ == "__main__":
    unittest.main(verbosity=2)
