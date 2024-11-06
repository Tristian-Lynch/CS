# -*- coding: utf-8 -*-

class MethodNotImplemented(Exception):
    """
    Indicates that you have not yet implemented this method.
    """
    pass


class MalformedExpression(Exception):
    """
    Indicates that an expression being parsed is malformed.
    """
    pass

class StackIsEmpty(Exception):
    """Indicates that the stack is empty."""
    pass
