# -*- coding: utf-8 -*-
"""Test cases for the two stacks implementation of a queue.

This module tests the QueueFromStacks implementation, which is subclass of
Queue. This essentially implements a queue using a circular array as the
underlying data structure to hold the elements.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 10, 2024
"""

import unittest

import exceptions
from stacks_queue import QueueFromStacks


class QueueFromStacksTest(unittest.TestCase):
    def setUp(self):
        self.queue = QueueFromStacks(5)

    def tearDown(self):
        del self.queue

    def test_enqueue_peek(self):
        """Test that an added item directly shows up with peek."""
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 3)
        self.assertEqual(self.queue.get_size(), 1)

    def test_enqueue_size(self):
        """Test the size updates after every enqueue."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertEqual(self.queue.get_size(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.get_size(), 2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.get_size(), 3)
        self.queue.enqueue(4)
        self.assertEqual(self.queue.get_size(), 4)

    def test_dequeue_size(self):
        """Test the size updates after every dequeue"""
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.get_size(), 3)

        self.queue.dequeue()
        self.assertEqual(self.queue.get_size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.get_size(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.get_size(), 0)

    def test_enqueue_dequeue(self):
        """Test that items enqueue can be dequeue in the right order."""
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.get_size(), 0)

        self.queue.enqueue(9)
        self.queue.enqueue("hello")
        self.queue.enqueue(-5)
        self.queue.enqueue("world!")
        self.queue.enqueue("!")

        self.assertEqual(self.queue.get_size(), 5)
        self.assertEqual(self.queue.dequeue(), 9)
        self.assertEqual(self.queue.dequeue(), "hello")
        self.assertEqual(self.queue.dequeue(), -5)
        self.assertEqual(self.queue.dequeue(), "world!")
        self.assertEqual(self.queue.dequeue(), "!")
        self.assertEqual(self.queue.get_size(), 0)

    def test_empty_dequeue(self):
        """Test that dequeue on an empty queue raises an exception"""
        with self.assertRaises(exceptions.QueueIsEmpty):
            self.queue.dequeue()

    def test_empty_peek(self):
        """Test that dequeue on an empty queue raises an exception"""
        with self.assertRaises(exceptions.QueueIsEmpty):
            self.queue.peek()

    def test_full_enqueue(self):
        """Test that a queue that reaches the capacity raises an exception."""
        for i in range(5):
            self.queue.enqueue(i)

        with self.assertRaises(exceptions.QueueFullError):
            self.queue.enqueue(9000)

    def test_layout(self):
        """Test that underlying queue contains correct ordering."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(4)
        self.queue.enqueue(-1)
        self.queue.enqueue(-2)
        print(str(self.queue))

        # test shape after enqueueing everything.
        self.assertEqual(str(self.queue), "[1, 2, 4, -1, -2]")

        # test removing one element, then adding another
        self.queue.dequeue()
        self.assertEqual(str(self.queue), "[2, 4, -1, -2]")
        self.queue.enqueue("hello")
        self.assertEqual(str(self.queue), "[2, 4, -1, -2, 'hello']")

        # remove two elements and make sure they are replaced!
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.enqueue(-9)
        self.queue.enqueue(100)
        self.assertEqual(str(self.queue), "[-1, -2, 'hello', -9, 100]")

        # make some sanity checks
        self.assertEqual(self.queue.peek(), -1)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(self.queue.dequeue(), "hello")
        self.assertEqual(self.queue.dequeue(), -9)
        self.assertEqual(self.queue.dequeue(), 100)
        self.assertEqual(self.queue.get_size(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
