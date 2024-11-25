# vim: set tw=79 tb=4 sw=4 et
"""Module for a generic binary tree used in CS302 Lab 3.

This module defines the BinaryTree class, which is a class defining a generic
tree with an arity of 2. For simplicity, we will assume all of our nodes
contain integers as their data.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 23, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""


from sys import maxsize
from typing import override

import exceptions
from binary_node import BinaryNode
from node import Node, null
from tree import Tree


class BinaryTree(Tree):
    """A generic binary tree class with arity of 2.

    Attributes:
        name (int):
            The name of the tree, for debugging and test purposes.
        root (Node):
            The root of the tree if created, defaults to null for an empty
            tree.
    """

    def __init__(self, name: str = "", root: BinaryNode = null):
        """Instantiate a tree.

        Args:
            name (str):
                The name of the tree, default to empty string.
            root (BinaryNode):
                The root node of the tree, defaults to node.null
        """
        super().__init__(2, name, root)

    @override
    def add_node(self, parent: Node, data: int) -> Node:
        """Helper method to add a node to the tree.

        This will create the node.

        Args:
            parent (Node):
                The parent of the node to be created.
            data (int):
                The data to save in the node.

        Returns: Node
            Should never return
        """
        raise exceptions.CannotUseAddChildWithBinaryNode(
            "Please use the .left and .right properties with a binary node."
        )

    def add_left_child(self, parent: BinaryNode, data: int) -> BinaryNode:
        """Helper method to add a left child for a parent.

        Args:
            parent (BinaryNode):
                The parent node to add a left child for.
            data (int):
                The data that will go into the node.

        Returns:
            BinaryNode: The node that was created.
        """
        node = BinaryNode(data)
        parent.left = node
        return node

    def add_right_child(self, parent: BinaryNode, data: int) -> BinaryNode:
        """Helper method to add a right child for a parent.

        Args:
            parent (BinaryNode):
                The parent node to add a right child for.
            data (int):
                The data that will go into the node.

        Returns:
            BinaryNode: The node that was created.
        """
        node = BinaryNode(data)
        parent.right = node
        return node

    def contains(self, item: int):
        """Check if this binary tree contains an item.

        Args:
            item (int):
                The item to search for.

        Returns:
            bool: True of the item is found, False otherwise.

        """
        """Check if this binary tree contains an item."""

        # Helper function to recursively search for an item in the tree.
        def _contains(node: BinaryNode, item: int) -> bool:
            # If we reach a null node, the item is not in that subtree.
            if node.is_null_node():
                return False
            # If the current node's data is the item, we found it.
            if node.data == item:
                return True
            # Check left and right subtrees for the item.
            return _contains(node.left, item) or _contains(node.right, item)

        # Edge case: empty tree.
        if self.is_empty():
            return False
        return _contains(self.root, item)

    @override
    def has_search_property(self) -> bool:
        """Check if this tree has the search property.

        Returns: bool
           False for a generic tree like this one.
        """
        """Check if this binary tree has the search property (BST)."""

        # Helper function to recursively check if the tree has the search property.
        def _is_bst(node: BinaryNode, min_val: int, max_val: int) -> bool:
            # If we reach a null node, we have a valid BST.
            if node.is_null_node():
                return True
            # If the current node's data is not within the bounds, we don't have a BST.
            if not (min_val < node.data < max_val):
                return False
            # We need to check the left and right subtrees with the new bounds.
            # Settting the new max value to the current node's data and the new
            # min value to the current node's data for each subtree.
            return _is_bst(node.left, min_val, node.data) and _is_bst(
                node.right, node.data, max_val
            )

        if self.is_empty():
            return True
        # Used maxsize to represent positive infinity and negative infinity.
        return _is_bst(self.root, -maxsize, maxsize)
