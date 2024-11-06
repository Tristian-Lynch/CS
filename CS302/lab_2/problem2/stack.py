# -*- coding: utf-8 -*-
"""Module for a generic stack used in CS302 Lab 2.

This module defines the Stack class, which is an wrapper class around a python
list with the push/pop functionality added.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 09, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

from exceptions import StackIsEmpty


class Stack:
    """A wrapper class around a regular list used to implement a stack.

    Attributes:
        _ilist: List[any]
            The inner list used to hold the actual elements in the stack.
    """

    def __init__(self):
        """Initialize the inner list to be empty"""
        self._ilist = []

    def push(self, item: any):
        """Push an item onto the top of the stack.

        Args:
            item (any): The item to be pushed on the stack.
        """
        self._ilist.append(item)

    def pop(self) -> any:
        """Pop the element last added to the stack.

        Returns:
            any: The item at the top of the stack, if any

        Raises:
            StackIsEmpty: If the stack is empty.
        """
        if self.is_empty():
            raise StackIsEmpty
        return self._ilist.pop()

    def get_size(self) -> int:
        """Get the current number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self._ilist)

    def is_empty(self) -> bool:
        """Check if the stack is empty or not.

        Returns:
           bool: True if the stack is empty, False otherwise.
        """
        return self.get_size() == 0

    def __str__(self) -> str:
        """Returns a string representation of the stack.

        This is simply the same as the string representation of the inner list.

        Returns:
            str: The string representation of the stack.
        """
        return str(self._ilist)
