# vim: set tw=79 tb=4 sw=4 et
"""Module for a generic tree used in CS302 Lab 3.

This module defines the Tree class, which is a class defining a generic
tree with a certain arity. For simplicity, we will assume all of our nodes
contain integers as their data.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 23, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

from node import Node, NullNode, null
from itertools import chain
import exceptions


class Tree(object):
    """A generic tree class with variable arity.

    Attributes:
        name (int):
            The name of the tree, for debugging and test purposes.
        root (Node):
            The root of the tree if created, defaults to null for an empty
            tree.
        arity (int):
            The arity of the tree, can only be set once.
    """

    def __init__(self, arity: int, name: str = "", root: Node = null):
        """Instantiate a tree.

        Args:
            arity (int):
                The given arity of the tree, must be passed in.
            name (str):
                The name of the tree, default to empty string.
            root (Node):
                The root node of the tree, defaults to node.null
        """
        self.name = name
        self.root = root
        self.arity = arity

    def get_size(self) -> int:
        """Compute the size (the number of nodes) of the tree.

        Returns: int
            The number of nodes in the tree.
        """
        return self.root.size()

    def get_height(self) -> int:
        """Compute the height of the tree.

        Returns: int
           The height of the root of the tree.
        """
        return self.root.height()

    def has_search_property(self) -> bool:
        """Check if this tree has the search property.

        Returns: bool
           False for a generic tree like this one.
        """
        return False

    def is_empty(self) -> bool:
        """Check if the tree is empty.

        Returns: bool
           True if the root is null, False otherwise.
        """
        return isinstance(self.root, NullNode)

    def add_node(self, parent: Node, data: int) -> Node:
        """Helper method to add a node to the tree.

        This will create the node.

        Args:
            parent (Node):
                The parent of the node to be created.
            data (int):
                The data to save in the node.

        Returns: Node
            The created node.
        """
        child = Node(self.arity, data)
        parent.add_child(child)
        return child

    def _str_helper(self, level: int, node: Node):
        if node.is_null_node():
            return ""
        blanks = " " * (level * 2)
        identifer = f"node: {node.data}\n"
        children = [
            self._str_helper(level + 1, ch) for ch in node.children
        ]
        return "".join(list(chain([blanks, identifer], children)))

    def __str__(self) -> str:
        """Build a string representation of the tree.

        This is not very sophisticated, it simply puts one node per line, with
        some number of prefixed spaces depending on the level of each node.

        Here's an example of how to build and print the following tree:
                            0
                          / | \
                         1  2  3
                           / \\ \
                          4   5  6
                                  \
                                   7

        Examples:
            >>> t = Tree(3, "test", Node(3, 0))
            >>> t.add_node(t.root, 1)
            >>> ch = t.add_node(t.root, 2)
            >>> ch2 = t.add_node(t.root, 3)
            >>> t.add_node(t.add_node(ch, 4), 5)
            >>> t.add_node(t.add_node(ch2, 6), 7)
            >>> print(t)
            name: test
            node: 0
              node: 1
              node: 2
                node: 4
                  node: 5
              node: 3
                node: 6
                  node: 7

        Returns: str
            The string representation of the tree.
        """
        identifer = f"name: {self.name}\n"
        return "".join([identifer, self._str_helper(0, self.root)])

    def preorder_traversal(self):
        raise exceptions.UseTraversalsOnlyForBinaryTrees

    def inorder_traversal(self):
        raise exceptions.UseTraversalsOnlyForBinaryTrees

    def postorder_traversal(self):
        raise exceptions.UseTraversalsOnlyForBinaryTrees
