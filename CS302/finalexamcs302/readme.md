# CS302: Final exam: Tree Traversals

## Introduction

The goal of this final exam is to complete the implementation of the binary
serach tree data structure with the necessary traversals we discussed in class.
Those traversals are the following:

1. Pre-order traversal.

2. In-order traversal.

3. Post-order traversal.

## Setup

For this lab, you will need to a have a version of `python3` installed. In
addition, you will need to have the `unittest` library installed so you could
run the unit tests provided for each problem. The easiest way to do so is to
grab a terminal window (or PowerShell on Windows) and enter the following
command:

```shell
pip install unittest
```

Alternative, if `pip` not installed, you can use:

```shell
python -m pip install unittest
```

You can also run the whole lab in an IDE. Please refer to the previous video
from lab 1 for setup with the VisualStudioCode IDE.

## Problem 1: Pre-order traversal

In the first problem, you should implement the `preorder_traversal` method of
`binary_node.py`. This method will apply to every binary node, regardless of
whether the tree is a search tree or not.

To visit a node, you should call the `visit_node` method implemented in the
`Node` class follows:

```python
def visit_node(self):
  print(self.data, end=' ')
```

As you can see, all this method does is to print the node's value, but instead
of writing a newline at the end, it will add a space character.

This method should be the only thing you do when you visit a node in the tree
in any kind of traversal.

### Quick Testing

In the file `tree_builder.py`, I have included a quick testing method for you to
view and sanitize if everything is working correct. Also it will be helpful if
you are debugging as you don't have to run the entirety of the test cases.

To run this test, simple open your terminal window to the directory where you
are writing your code, and then do:

```shell
python3 tree_builder.py

------ The tree ---------
name: first_tree
node: 0
  node: 1
    node: 3
  node: 2
    node: 5
    node: 7

------ Preorder traversal ---------
0 1 3 2 5 7
```

or

```shell
python tree_builder.py

------ The tree ---------
name: first_tree
node: 0
  node: 1
    node: 3
  node: 2
    node: 5
    node: 7

------ Preorder traversal ---------
0 1 3 2 5 7
```

depending on your `python` distribution.

### Testing

To run the tests, if you are using an IDE, then you can use the IDE appropriate
method for running individual tests.

If you are using a terminal, then you can run all tests using:

```shell
python3 binary_tree_test.py
```

or,

```shell
python binary_tree_test.py
```

depending on your `python` installation.

Note that this will run all tests, not just those for the `get_size` method. To
restrict the tests to only that one, you could use:

```shell
python3 binary_tree_test.py BinaryTreePreOrderTraversalTest
```

## Problem 2: In-order traversal

In the first problem, you should implement the `inorder_traversal` method of
`binary_node.py`. This method will apply to every binary node, regardless of
whether the tree is a search tree or not.

To visit a node, you should call the `visit_node` method implemented in the
`Node` class follows:

```python
def visit_node(self):
  print(self.data, end=' ')
```

As you can see, all this method does is to print the node's value, but instead
of writing a newline at the end, it will add a space character.

This method should be the only thing you do when you visit a node in the tree
in any kind of traversal.

### Quick Testing


You can use the same little test method in `tree_builder.py` but make sure to
comment out the `preorder_traversal` method call and replace it with the
`inorder_traversal` call.

To run this test, simple open your terminal window to the directory where you
are writing your code, and then do:

```shell
python3 tree_builder.py

------ The tree ---------
name: first_tree
node: 0
  node: 1
    node: 3
  node: 2
    node: 5
    node: 7

------ Inorder traversal ---------
3 1 0 5 2 7
```

or

```shell
python tree_builder.py

------ The tree ---------
name: first_tree
node: 0
  node: 1
    node: 3
  node: 2
    node: 5
    node: 7

------ Inorder traversal ---------
3 1 0 5 2 7
```

depending on your `python` distribution.

### Testing

To run the tests, if you are using an IDE, then you can use the IDE appropriate
method for running individual tests.

If you are using a terminal, then you can run all tests using:

```shell
python3 binary_tree_test.py
```

or,

```shell
python binary_tree_test.py
```

depending on your `python` installation.

Note that this will run all tests, not just those for the `get_size` method. To
restrict the tests to only that one, you could use:

```shell
python3 binary_tree_test.py BinaryTreeInOrderTraversalTest
```


## Problem 3: Post-order traversal

In the first problem, you should implement the `postorder_traversal` method of
`binary_node.py`. This method will apply to every binary node, regardless of
whether the tree is a search tree or not.

To visit a node, you should call the `visit_node` method implemented in the
`Node` class follows:

```python
def visit_node(self):
  print(self.data, end=' ')
```

As you can see, all this method does is to print the node's value, but instead
of writing a newline at the end, it will add a space character.

This method should be the only thing you do when you visit a node in the tree
in any kind of traversal.

### Quick Testing


You can use the same little test method in `tree_builder.py` but make sure to
comment out the `inorder_traversal` method call and replace it with the
`postorder_traversal` call.

To run this test, simple open your terminal window to the directory where you
are writing your code, and then do:

```shell
python3 tree_builder.py

------ The tree ---------
name: first_tree
node: 0
  node: 1
    node: 3
  node: 2
    node: 5
    node: 7

------ Postorder traversal ---------
3 1 5 7 2 0
```

or

```shell
python tree_builder.py

------ The tree ---------
name: first_tree
node: 0
  node: 1
    node: 3
  node: 2
    node: 5
    node: 7

------ Postorder traversal ---------
3 1 5 7 2 0
```

depending on your `python` distribution.

### Testing

To run the tests, if you are using an IDE, then you can use the IDE appropriate
method for running individual tests.

If you are using a terminal, then you can run all tests using:

```shell
python3 binary_tree_test.py
```

or,

```shell
python binary_tree_test.py
```

depending on your `python` installation.

Note that this will run all tests, not just those for the `get_size` method. To
restrict the tests to only that one, you could use:

```shell
python3 binary_tree_test.py BinaryTreePostOrderTraversalTest
```

## Submission

Please submit your modified `.py` files along with a scanned copy of your
written final exam to Canvas before the timer runs out.

