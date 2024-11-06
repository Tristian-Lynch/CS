# -*- coding: utf-8 -*-
"""Implementation of a queue using a circular array.

This module defines the CircularArrayQueue, which is subclass of Queue. This
essentially implements a queue using a circular array as the underlying data
structure to hold the elements.

@Author: ADD YOUR NAME HERE (ADD YOUR EMAIL HERE)
@Date: ADD THE DATE WHEN YOU START HERE
"""

from iqueue import IQueue
from exceptions import MethodNotImplemented, QueueFullError, QueueIsEmpty
from typing import override


class CircularArrayQueue(IQueue):
    """An implementation of queue using a circular array as the underlying data
       structure.

    Attributes:
        capacity: int
            The maximum capacity of the queue. We will consider this to be
            static for now and not worry about when we run out of space.
    """

    def __init__(self, capacity: int):
        """Instantiate a circular arry queue.

        Args:
            capacity (int): The maximum capacity of the queue
        """
        super().__init__()
        self.capacity = capacity

        # TODO: Initialize a list with a maximum capacity of self.capacity.
        #       Note that you can initialize the list with None objects since
        #       our queue can be used to hold things of any type.

    @override
    def enqueue(self, item: object):
        """Add an item to the tail of the queue.

        Implement this function in a way that adds the item at the tail of the
        queue. Your code should raise the `QueueFullError` exception when the
        queue is full and you cannot add the item to the list.

        _Hint_: Avoid using `append` here as that would make implementing the
        circular array much harder.

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

        This method should return a string representation of the inner list
        used for your queue. It should dump the inner array as is, without
        ordering it accordinng to the head and the tail of the queue. In other
        words, this method does not care that the inner array is circular, it
        just prints it as is.

        Example:
            Here's a running example of a queue of capacity 3.

            >>> q = CircularArrayQueue(3)
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.enqueue(3)
            >>> print(q)
            [1, 2, 3]
            >>> q.dequeue()
            >>> print(q)
            [1, 2. 3]
            >>> q.enqueue(4)
            >>> print(q)
            [4, 2, 3]
            >>> print(q.dequeue())
            2
            >>> print(q.dequeue())
            3
            >>> print(q)
            [4, 2, 3]
            >>> q.enqueue("hi")
            >>> print(q)
            [4, "hi", 3]

        Returns:
            str: A string representation of the queue that meets the above
                specifications.
        """
        # TODO: Add you implementation for representing the inner array as a
        #   string. Note that if you use the List type in python, this should
        #   be a simple one liner.
        raise MethodNotImplemented
