# vim: tw=79 sw=4 ts=4

class InvalidNodeInstance(Exception):
    pass


class RootAlreadyAssignedException(Exception):
    pass


class NodeCannotHaveMoreChildren(Exception):
    pass


class InvalidChildAccess(Exception):
    pass


class MethodNotYetImplemented(Exception):
    pass


class NodeArityCannotChangeDynamically(Exception):
    pass


class CannotUseAddChildWithBinaryNode(Exception):
    pass
