# -*- coding: utf-8 -*-
"""Module for a generic  binary node used in CS302 Lab 3.

This module defines the BinaryNode class, which is a class defining a generic
node in a binary tree. For simplicity, we will assume all of our nodes contain
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
from node import Node


class BinaryNode(Node):
    """A generic binary node that has a left and a right child.

    Attributes:
        data: int
            The data contained in the node.
    """

    def __init__(self, data=None):
        """Instanciate a binary node with optional data.

        Args:
            data (int): The (optional) data item to hold in the node.
        """
        super().__init__(2, data)

    @override
    def add_child(self, child: Node) -> int:
        """Override the `add_child` method to prevent using it.

        Args:
            child (Node):
                The child wanted to be added, will not be added.

        Raises: exceptions.CannotUseAddChildWithBinaryNode
            Always raises the CannotUseAddChildWithBinaryNode exception to
            prevent anyone from using this method.

        Returns: int
            Should never return.
        """
        raise exceptions.CannotUseAddChildWithBinaryNode(
            "Please use the .left and .right properties with a binary node."
        )

    @property
    def left(self):
        """Getter for the left child of the node.

        Returns:
            A reference to the left child of this node.
        """
        return self.get_child(0)

    @property
    def right(self):
        """Getter for the right child of the node.

        Returns:
            A reference to the right child of this node.
        """
        return self.get_child(1)

    @left.setter
    def left(self, value: BinaryNode):
        """Setter for the left child of the node.

        This method prevents the user from setting bogus values for either the
        left or the right child.

        Args:
            value (BinaryNode):
                The binary node to assign as the left child of the current
                node.
        """
        if not isinstance(value, BinaryNode):
            raise exceptions.InvalidNodeInstance
        self.children[0] = value

    @right.setter
    def right(self, value):
        """Setter for the right child of the node.

        This method prevents the user from setting bogus values for either the
        left or the right child.

        Args:
            value (BinaryNode):
                The binary node to assign as the right child of the current
                node.
        """
        if not isinstance(value, BinaryNode):
            raise exceptions.InvalidNodeInstance
        self.children[1] = value
