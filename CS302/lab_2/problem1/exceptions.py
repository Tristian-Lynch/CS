# -*- coding: utf-8 -*-

class MethodNotImplemented(Exception):
    """
    Indicates that you have not yet implemented this method.
    """
    pass


class QueueFullError(Exception):
    """
    Indicates that the queue is full and we no longer have room for a new item.
    """
    pass


class QueueIsEmpty(Exception):
    """
    Indicates that the queue is empty and cannot dequeue from it.
    """
    pass


class StackIsEmpty(Exception):
    """
    Indicates that the stack is empty and cannot be popped.
    """
    pass
