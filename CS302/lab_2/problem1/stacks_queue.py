# -*- coding: utf-8 -*-
"""Implementation of a queue using a two stacks.

This module defines the QueueFromStacks, which is subclass of IQueue. This
essentially implements a queue using a two stacks as the underlying data
structure to hold the elements.

@Author: ADD YOUR NAME HERE (ADD YOUR EMAIL HERE)
@Date: ADD THE DATE WHEN YOU START HERE
"""

from typing import override

from exceptions import MethodNotImplemented, QueueIsEmpty
from iqueue import IQueue
from stack import Stack


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

        self.s1 = Stack()
        self.s2 = Stack()

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
        
        self.s1.push(item)

    @override
    def dequeue(self) -> object:
        """Remove the item at the head of the queue and return it.

        Returns:
            object: The item that is dequeued and remove from the queue.

        Raises:
            MethodNotImplemented: If the method is not implemented.
            QueueIsEmpty: If the queue is empty and there's nothing to dequeue.
        """
        if self.s1.is_empty():
            raise QueueIsEmpty
        return self.s1.pop()

    @override
    def peek(self) -> object:
        """Peek at the item at the head of the queue, but do not remove it.

        Returns:
            object: The item that is at the head of the queue, if any.

        Raises:
            MethodNotImplemented: If the method is not implemented.
            QueueIsEmpty: If the queue is empty and there's nothing to peek at.
        """
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        if self.s2.is_empty():
            raise QueueIsEmpty("Queue is empty. Cannot peek.")
        return self.s2.peek()

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
        temp_stack = Stack()
        items = []

        # Transfer items from s1 to temp_stack and collect them in a list
        while not self.s1.is_empty():
            item = self.s1.pop()
            items.append(item)
            temp_stack.push(item)

        # Restore the original stack s1
        while not temp_stack.is_empty():
            self.s1.push(temp_stack.pop())

        # The items list now contains the queue elements from head to tail
        return "[" + ", ".join(repr(item) for item in items) + "]"
