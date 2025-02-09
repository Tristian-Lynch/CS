# -*- coding: utf-8 -*-
"""Module for a generic  node used in CS302 Lab 3.

This module defines the Node class, which is a class defining a generic
node in a any tree. For simplicity, we will assume all of our nodes contain
integers as their data.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 23, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

from __future__ import annotations

from typing import override

import exceptions


class Node(object):
    """A generic node class with a certain given arity.

    Attributes:
        arity: int
            The number of children the node can have.
        data: int
            The data element contained in the node, assumed to be an integer.
        children:
            The list of children for this node, can contain at most
            `arity` children.
    """

    def __init__(self, arity: int, data: int = None):
        """Constructor for the Node class.

        Args:
            data (int):
                The data contained in the node, assumed ot be integers
            children (List[Node]):
                The list of children for this node.
                Originally, this list contains all NullNode instances.
        """
        self._arity = arity
        self.data = data
        self.children = [null] * self._arity

    def add_child(self, child: Node) -> int:
        """Add a child for this node

        This method will search for an empty spot (i.e., one that have a null
        node) and replace it with the given child. If no such empty spot
        exists, then raise an exception.

        Args:
            child: Node
                The child to add.

        Raises: exceptions.NodeCannotHaveMoreChildren
            Raises NodeCannotHaveMoreChildren exceptions when the number of
            non null children for the node is already maxed out.

        Returns: int
            The index at which the child was added.
        """
        for i, ch in enumerate(self.children):
            if ch.is_null_node():
                self.children[i] = child
                return i
        raise exceptions.NodeCannotHaveMoreChildren

    def get_child(self, index: int) -> Node:
        """Get a child at a certain index.

        Args:
            index: int
                The index of the child to obtain, starting from 0.

        Raises: exceptions.InvalidChildAccess
            Raises an InvalidChildAccess exception if the index is not a valid
            one.

        Returns:
            The child node at index `index`.

        Warning:
            The child returned might be a NullNode instance, so that must be
            checked by the caller of this method.
        """
        if index < len(self.children):
            return self.children[index]
        raise exceptions.InvalidChildAccess

    @property
    def arity(self) -> int:
        """Get the arity for the node, if needed.

        Returns: int
            Returns the current arity of the node.
        """
        return self._arity

    @arity.setter
    def arity(self, value: int):
        """Make the arity attribute read-only.

        Args:
            value: int
                The value to update, not really used!

        Raises:
            Raises the NodeArityCannotChangeDynamically to prevent modification
            of the arity at runtime.

        Returns:
            Should not return ever.
        """
        raise exceptions.NodeArityCannotChangeDynamically

    def is_null_node(self) -> bool:
        """Check if this node is a null node

        Returns: False.
        """
        return False

    def size(self) -> int:
        """Obtain the size of the subtree rooted at this node.

        Returns: int
            The computed size of the subtree rooted at this node.
        """
        # If the node is a null node, return 0
        if self.is_null_node():
            return 0
        # Otherwise, return 1 plus the sum of the sizes of the children.
        return 1 + sum(
            child.size() for child in self.children if not child.is_null_node()
        )

    def height(self) -> int:
        """Obtain the height of this node in its current tree.

        Returns: int
            The computer height of the node.
        """
        # If the node is a null node or all of its children are null nodes,
        if self.is_null_node() or all(child.is_null_node() for child in self.children):
            return 0
        # Otherwise, return 1 plus the maximum height of the children
        return 1 + max(
            child.height() for child in self.children if not child.is_null_node()
        )

    @override
    def __str__(self) -> str:
        return "( " + str(self.data) + " )"


class NullNode(Node):
    def __init__(self, arity: int = -1, data: int = None):
        self._arity = -1
        self.children = []

    @override
    def is_null_node(self):
        """Check if this node is a null node

        Returns: True.
        """
        return True

    @override
    def size(self) -> int:
        """Obtain the size of the subtree rooted at this node.

        Returns: int
            For the null node, this always returns 0.
        """
        return 0

    @override
    def height(self) -> int:
        return 0


# This module variable is used to designate a null node instead of having to
# instantiate the class every time we need one.
null = NullNode()
