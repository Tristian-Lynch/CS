# -*- coding: utf-8 -*-
"""Module for a postfix evaluator used in CS302 Lab 2.

This module defines the PostfixEvaluator class, which implements an algorithm
to validate and evaluate arithmetic expressions written in postfix notation.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 12, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

from exceptions import MalformedExpression
from stack import Stack


class PostfixEvaluator:
    """A postfix evaluator class used in Lab 2 of CS302.

    Attributes:
        parsed_expressions: int
            The current number of parsed expressions since instance creation.
        allowed_operators: Dict[str: lambda x, y]
    """

    def __init__(self):
        """Initialize an instance of the PostfixEvaluator class"""
        self.parsed_expressions = 0
        self.allowed_operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y,
            "^": lambda x, y: x**y,
        }

    def is_allowed_operator(self, op: str) -> bool:
        """Check if an operator is allowed in this lab.

        You only have to consider operators that are listed in the dictionnary
        above (`allowed_operators`).

        Args:
            op (str): The operator to check

        Returns: True if the operator is allowed, False otherwise.

        """
        if op not in ["+", "-", "/", "*", "^"]:
            return False
        return True

    def evaluate_expr(self, expression: str) -> int:
        """Evaluate a single expression presented in postfix notation.

        This method evaluates a single expression presented in postfix notation
        and returns the result of the evaluation as a single integer.

        If the expression is not formatted well, then the method MUST raise the
        MalformedExpression exception to pass all the tests. Therefore, you
        must think of a way to detect when an expression is malformed.

        Finally, this method must increment the `parsed_expressions` counter
        for each evaluated expression.

        Args:
            expression (str): The expression to evaluate.

        Example:
            Here's a running example of a few expressions.

            >>> ev = PostfixEvaluator()
            >>> ev.evaluate_expr('2 3 +')
            5
            >>> ev.evaluate_expr('3 4 5 * +')
            23

        Hint:
            To use the allowed_operators set, you can do so as follows.
            Assume that `op` is an operator, you can apply `op` to two
            variables `x` and `y` as follows:

            >>> op = '+'
            >>> x = 1
            >>> y = 2
            >>> res = self.allowed_operators.get(op)(x, y)
            >>> print(res)
            3

        Returns:
            int: The result of the evaluation of the full expression.
        """
        stack = Stack()
        tokens = expression.strip().split()

        try:
            for token in tokens:
                try:
                    # Check if the token is an integer.
                    value = int(token)
                    stack.push(value)
                except ValueError:
                    # Not an integer, check if it's an operator, if not raise exception.
                    if self.is_allowed_operator(token):
                        # token is an operator
                        # Check if there are enough operands and values
                        if stack.get_size() < 2:
                            raise MalformedExpression
                        y = stack.pop()
                        x = stack.pop()
                        try:
                            result = self.allowed_operators[token](x, y)
                        except ZeroDivisionError:
                            raise MalformedExpression
                        stack.push(result)
                    else:
                        # Invalid token
                        raise MalformedExpression

            if stack.get_size() != 1:
                raise MalformedExpression

            result = stack.pop()
            self.parsed_expressions += 1
            return result

        except Exception:
            raise MalformedExpression
