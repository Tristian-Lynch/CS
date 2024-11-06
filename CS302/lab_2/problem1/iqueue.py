# -*- coding: utf-8 -*-
"""Module for a generic queue used in CS302 Lab 2.

This module defines the IQueue class, which is an abstract class defining a
generic queue that you are going to implement using various underlying data
strcutures.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 09, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""


class IQueue:
    """An abstract class for a generic queue used in Lab 2 of CS302.

    Attributes:
        size: int
            The current number of elements in the queue.
    """

    def __init__(self):
        self.size = 0

    def enqueue(self, item: object):
        """Add an item to the tail of the queue.

        Args:
            item (object): The item to add to the queue.
        """
        pass

    def dequeue(self) -> object:
        """Remove the item at the head of the queue and return it."""
        pass

    def peek(self) -> object:
        """Peek at the item at the head of the queue, but do not remove it.

        Returns:
            object: The item that is at the head of the queue, if any.
        """
        pass

    def get_size(self) -> int:
        """Obtain the current size of the queue.

        Returns:
            int: The current size of the queue.
        """
        return self.size

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.get_size() == 0
