# -*- coding: utf-8 -*-
"""Implementation of a queue using a two stacks.

This module defines the QueueFromStacks, which is subclass of IQueue. This
essentially implements a queue using a two stacks as the underlying data
structure to hold the elements.

@Author: ADD YOUR NAME HERE (ADD YOUR EMAIL HERE)
@Date: ADD THE DATE WHEN YOU START HERE
"""

from iqueue import IQueue
from stack import Stack
from exceptions import MethodNotImplemented, QueueFullError, QueueIsEmpty
from typing import override


class QueueFromStacks(IQueue):
    """An implementation of queue using two stacks as the underlying data
       structure.

    Attributes:
        capacity: int
            The maximum capacity of the queue. We will consider this to be
            static for now and not worry about when we run out of space.
    """

    def __init__(self, capacity: int):
        """Instantiate a queue from two stacks.

        Args:
            capacity (int): The maximum capacity of the queue
        """
        super().__init__()
        self.capacity = capacity

        # TODO: Initialize two stacks using the Stack data structure provided
        #       in `stack.py`

    @override
    def enqueue(self, item: object):
        """Add an item to the tail of the queue.

        Implement this function in a way that adds the item at the tail of the
        queue. Your code should raise the `QueueFullError` exception when the
        queue is full and you cannot add the item to the queue.

        Args:
            item: The item to add to the queue.

        Raises:
            MethodNotImplemented: If the method is not implemented.
            QueueFullError: If the queue is full and we cannot add the item.
        """
        # TODO: Add the item to the tail end of the queue.
        #
        #   Warning: The tail is not necessarily the element at the last index
        #       of the queue, recall that we are using a circular array.
        raise MethodNotImplemented

    @override
    def dequeue(self) -> object:
        """Remove the item at the head of the queue and return it.

        Returns:
            object: The item that is dequeued and remove from the queue.

        Raises:
            MethodNotImplemented: If the method is not implemented.
            QueueIsEmpty: If the queue is empty and there's nothing to dequeue.
        """
        # TODO: Remove the top element from the queue and return it.
        #   Your implementation MUST raise the QueueIsEmpty exception if there
        #   are no elements in the queue to be dequeued.
        raise MethodNotImplemented

    @override
    def peek(self) -> object:
        """Peek at the item at the head of the queue, but do not remove it.

        Returns:
            object: The item that is at the head of the queue, if any.

        Raises:
            MethodNotImplemented: If the method is not implemented.
            QueueIsEmpty: If the queue is empty and there's nothing to peek at.
        """
        # TODO: Peek at top element from the queue. This is essentially the
        #   same as dequeue except that we do NOT remove the element from the
        #   queue.
        #
        #   Your implementation MUST raise the QueueIsEmpty exception if there
        #   are no elements in the queue to be dequeued.
        raise MethodNotImplemented

    def __str__(self):
        """Returns a string representation of the queue.

        This method should return a list representation of your queue. Note
        that this is different from the `str` method in CircularArrayQueue.
        In this case, we would like to print the content of the queue with the
        head of the queue as the leftmost item, and the tail of the queue as
        the rightmost item, with commas in between.

        Please make sure to add the opening and closing `[` characters to
        match the output in the test cases. You can refer to the examples below
        for more information.

        Example:
            Here's a running example of a queue of capacity 3.

            >>> q = QueueFromStacks(3)
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.enqueue(3)
            >>> print(q)
            [1, 2, 3]
            >>> q.dequeue()
            >>> print(q)
            [2, 3]
            >>> q.enqueue(4)
            >>> print(q)
            [2, 3, 4]
            >>> print(q.dequeue())
            2
            >>> print(q.dequeue())
            3
            >>> print(q)
            [4]
            >>> q.enqueue("hi")
            >>> print(q)
            [4, "hi"]

        Returns:
            str: A string representatino of the queue that meets the above
                specifications.
        """
        # TODO: Add you implementation for building the string representation
        #       of the qeue from stacks.
        raise MethodNotImplemented
