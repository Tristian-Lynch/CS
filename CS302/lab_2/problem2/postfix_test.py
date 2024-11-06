# -*- coding: utf-8 -*-
"""Test cases for the postfix arithmetic evaluator.

This module tests the PostfixEvaluator class, a postifx expression evaluator.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 12, 2024
"""

from exceptions import MalformedExpression
from postfix import PostfixEvaluator
import unittest


class PostfixEvaluatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.evaluator = PostfixEvaluator()

    @classmethod
    def tearDownClass(self):
        del self.evaluator

    def test_simple_addition(self):
        """Test a simple addition with only two operands"""
        self.assertEqual(5, self.evaluator.evaluate_expr("3 2 +"))

    def test_simple_subtraction(self):
        """Test a simple subtraction with only two operands"""
        expr = "3 2 -"
        self.assertEqual(1, self.evaluator.evaluate_expr(expr))

    def test_simple_multiplication(self):
        """Test a simple multiplication with only two operands"""
        expr = "3 2 *"
        self.assertEqual(6, self.evaluator.evaluate_expr(expr))

    def test_simple_division(self):
        """Test a simple multiplication with only two operands"""
        expr = "3 2 /"
        self.assertEqual(1, self.evaluator.evaluate_expr(expr))

    def test_simple_exp(self):
        """Test a simple multiplication with only two operands"""
        expr = "3 2 ^"
        self.assertEqual(9, self.evaluator.evaluate_expr(expr))

    def test_more_addition(self):
        """Test more than one addition operation"""
        expr = "3 2 3 + +"
        self.assertEqual(8, self.evaluator.evaluate_expr(expr))

    def test_addition_commutative(self):
        """Test that addition is commutative"""
        expr = "3 2 + 3 +"
        self.assertEqual(8, self.evaluator.evaluate_expr(expr))

    def test_addition_subtraction(self):
        """Test an expression with both addition and subtraction"""
        expr = "3 2 4 + -"
        self.assertEqual(-3, self.evaluator.evaluate_expr(expr))

    def test_multiplication_division(self):
        """Test an expression with both multiplcation and division"""
        expr = "16 2 4 * /"
        self.assertEqual(2, self.evaluator.evaluate_expr(expr))

    def test_precedence_rules(self):
        """Test the precedence rules in arithmetic"""
        expr = "2 4 5 * +"
        self.assertEqual(22, self.evaluator.evaluate_expr(expr))
        expr = "2 4 + 5 *"
        self.assertEqual(30, self.evaluator.evaluate_expr(expr))
        expr = "3 2 + 1 5 + *"
        self.assertEqual(30, self.evaluator.evaluate_expr(expr))
        expr = "3 2 1 5 + + *"
        self.assertEqual(24, self.evaluator.evaluate_expr(expr))

    def test_malformed_expr_no_operator(self):
        """Test that an expression with no operators breaks"""
        expr = "3 4"
        with self.assertRaises(MalformedExpression):
            self.evaluator.evaluate_expr(expr)

    def test_malformed_expr_mistmatch(self):
        """Test that an expression with mismatched operands breaks"""
        expr = "3 4 + 2"
        with self.assertRaises(MalformedExpression):
            self.evaluator.evaluate_expr(expr)
        expr = "3 4 2 +"
        with self.assertRaises(MalformedExpression):
            self.evaluator.evaluate_expr(expr)

    def test_malformed_expr_no_operands(self):
        """Test that an expression with no operatands breaks"""
        expr = "+"
        with self.assertRaises(MalformedExpression):
            self.evaluator.evaluate_expr(expr)

    def test_malformed_expr_mistmatch_operators(self):
        """Test that an expression with mismatched operators breaks"""
        expr = "3 2 + -"
        with self.assertRaises(MalformedExpression):
            self.evaluator.evaluate_expr(expr)
        expr = "3 2 + 1 5 * / +"
        with self.assertRaises(MalformedExpression):
            self.evaluator.evaluate_expr(expr)

    def test_complex_operations(self):
        """Test that a bit more involved operations work"""
        expr = "6 5 4 + *"
        self.assertEqual(54, self.evaluator.evaluate_expr(expr))
        expr = "4 2 3 4 * + ^"
        self.assertEqual(268435456, self.evaluator.evaluate_expr(expr))
        expr = "6 5 4 3 * + 2 ^ *"
        self.assertEqual(1734, self.evaluator.evaluate_expr(expr))

    def test_malformed_expr_with_invalid_chars(self):
        """Test that invalid characters break"""
        expr = "a 3 +"
        with self.assertRaises(MalformedExpression):
            self.evaluator.evaluate_expr(expr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
