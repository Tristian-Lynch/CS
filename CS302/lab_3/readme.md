# CS302: Lab 03: Introduction to trees

## Learning Objectives

At the end of this lab, you should be able to:

1. Implement a generic tree with depth and height calculations.

2. Design and implement a solution to check whether a binary tree has the
   search property.

3. Implement a recursive search procedure in a binary tree.

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

## Problem 1: Generic tree methods

For the first problem, we will focus our attention on the files `tree.py` and
`node.py`. Those implement a generic tree that has a user-specified _arity_.
Recall that the arity of a tree defines the maximum number of children that a
node can have in the tree. Once the arity of a tree has been set, it can no
longer be changed.

### Step 1: Familiarize yourself with the code

The code in `tree.py` and `node.py` is heavily documented. Please read through
the class definition and the methods to understand how the code works.

Here is a simple example of how you can create a tree of arity 3.

```python
# create a root node with data 0
root = Node(3, 0)
# create the tree with arity 3 and the root node
t = Tree(3, "test", root)

# add nodes to the tree
# add_node will create a new node and link it to its parent.
n1 = t.add_node(root, 1)
n2 = t.add_node(root, 2)
n3 = t.add_node(root, 3)

# The tree now has a root that has three children with values 1, 2, and 3,
# respectively
# Let's add a node as a child of n3
t.add_node(n3, 4)

# You can print the tree using the normal print method
print(t)
```

And here's the output you should see,

```txt
name: test
node: 0
  node: 1
  node: 2
  node: 3
    node: 4
```

### Step 2: Implementing `get_size`

Your first task in this lab is to implement the `get_size` method in `tree.py`,
which simply return the size (i.e., the number of nodes) in the tree. You
__must__ do so recursively as we have discussed in class.

To be able to implement this recursively, you will need some help from the
`node.py` class so that each node can compute the size of its own subtree.
Therefore, start by implementing the `size` method in the `Node` class in
`node.py`. It is marked with a `TODO` comment. __NOTE__ that you will need to
implement this method in both the `Node` class and the `NullNode` class.

Once you have the `size` method implemented in the `Node` class, you can turn
to finalizing `get_size` in the `Tree` class. This will be simple one-liner.
You should ask yourself: Which subtree am I interested in computing the size
for? And then call the appropriate `size` method for that subtree's root.

#### Testing

To run the tests, if you are using an IDE, then you can use the IDE appropriate
method for running individual tests.

If you are using a terminal, then you can run all tests using:

```shell
python3 tree_test.py
```

or,

```shell
python tree_test.py
```

depending on your `python` installation.

Note that this will run all tests, not just those for the `get_size` method. To
restrict the tests to only that one, you could use:

```shell
python3 tree_test.py TreeSizeTest
```

### Step 3: Implementing `get_height`

Your second task in this lab is to implement the `get_height` method in
`tree.py`, which simply return the height in the tree. You __must__ do so
recursively as we have discussed in class. Recall that the _height_ of a tree
is the number of edges on the __longest path__ from the root to a leaf node.

To be able to implement this recursively, you will need some help from the
`node.py` class so that each node can compute the height of its own subtree.
Therefore, start by implementing the `height` method in the `Node` class in
`node.py`. It is marked with a `TODO` comment. __NOTE__ that you will need to
implement this method in both the `Node` class and the `NullNode` class. We
have the height of an empty tree (i.e., of the null node) in class.

Once you have the `height` method implemented in the `Node` class, you can turn
to finalizing `get_height` in the `Tree` class. This will be simple one-liner.
You should ask yourself: Which subtree am I interested in computing the size
for? And then call the appropriate `height` method for that subtree's root.

#### Testing

To run the tests, if you are using an IDE, then you can use the IDE appropriate
method for running individual tests.

If you are using a terminal, then you can run all tests using:

```shell
python3 tree_test.py
```

or,

```shell
python tree_test.py
```

depending on your `python` installation.

Note that this will run all tests, not just those for the `get_height` method. To
restrict the tests to only that one, you could use:

```shell
python3 tree_test.py TreeHeightTest
```

## Problem 2: Binary tree methods

### Step 1: Familiarize yourself with the code

The code in `binary_tree.py` and `binary_node.py` is heavily documented. Please
read through the class definition and the methods to understand how the code
works. Note that `BinaryNode` is a subclass of `Node` and `BinaryTree` is a
subclass of `Tree`. So any method that is implemented in `Tree` is also
available in `BinaryTree`, unless it has been _overridden_ (look for the
`@override` decorator for more information).

Here is a simple example of how you can create a binary tree.

```python
# create a root node with data 0
root = BinaryNode(0)
# create the binary tree, no need to specify arity, since it's fixed at 2.
t = BinaryTree("test", root)

# For binary tree's, I have disabled add_node because it is ambiguous.
# Instead, you can directly access the left and right children.
root.left = BinaryNode(1)
root.right = BinaryNode(2)

# Add a few more nodes
root.left.left = BinaryNode(3)
root.left.right = BinaryNode(4)
root.right.left = BinaryNode(5)
root.right.right = BinaryNode(6)

# You can print the tree using the normal print method
print(t)
```

And here's the output you should see,

```txt
name: test
node: 0
  node: 1
  node: 2
  node: 3
    node: 4
```

And here's the output you should see:

```text
name: test
node: 0
  node: 1
    node: 3
    node: 4
  node: 2
    node: 5
    node: 6
```

### Step 2: Implementing `contains`

Your first task in this problem is to implement the `contains` method in
`binary_tree.py`. `contains` accepts one argument, which is an integer to look
for, and searches the tree for it. If the integer is found, it returns `True`,
otherwise, it returns `False`. **Please note** that you should not assume that
the binary tree has the search property. In other words, there are no ordering
constraints on the nodes in the tree.

You are free to implement this method in the way that is most comfortable for
you. You can do so recursively or iteratively. If you choose to do it
recursively, feel free to add any methods you deem useful to the `BinaryNode`
class, though that is not particularly necessary.

#### Testing

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

Note that this will run all tests, not just those for the `contains` method. To
restrict the tests to only that one, you could use:

```shell
python3 binary_tree_test.py BinaryTreeContainsTest
```

### Step 3: Implementing `has_search_property`

Your second task in this problem is to implement the `has_search_property`
method in `binary_tree.py`. `has_search_property`, as its name suggests, checks
if a binary tree possesses the search property as defined in class, and returns
`True` if it does, `False` otherwise.

Again, you are free to implement this method in the way that is most
comfortable for you. You can do so recursively or iteratively. If you choose to
do it recursively, feel free to add any methods you deem useful to the
`BinaryNode` class, though that is not particularly necessary.

#### Step 3.1: Designing the solution

Before writing your code, please write a few sentences describing your proposed
solution in the `bst_search.txt` file. Your description __must match__ your
implementation, otherwise, you will not get credit for either!

#### Step 3.2: Analyze your solution

Also in `bst_search.txt`, please write down what you think is the asymptotic
runtime of your proposed solution in 3.1. You don't have to prove it, simply
state it with a brief rationale.

#### Step 3.3: Write the code

Now you are ready to write your code, so add it to `binary_tree.py` and
`binary_node.py` if necessary.

#### Hint

_Hint_: If you choose to leverage the presence of the `NullNode` then you
must be careful to add your methods to the three classes: `Node` and
`NullNode` in `node.py` as well as `BinaryNode` in `binary_node.py`. The ones
in `NullNode` and `BinaryNode` should have the `@override` decorator added,
just like code for `size` looks like.

For example, say I want to add a method `is_part_of_bst` to `BinaryNode` and
would like to leverage the presence of the `NullNode` class to set up a base
case for recursive. In that case, I would do the following.

1. In `node.py`, add the method to the `Node` class:

  ```python
  def is_part_of_bst(self) -> bool:
    # default is to return False
    return False
  ```

2. In `node.py`, override the method in the `NullNode` class:

  ```python
  @override
  def is_part_of_bst(self) -> bool:
    # an empty tree is a BST, so good!
    return True
  ```

3. In `binary_node.py`, override the method in the `BinaryNode` class:

  ```python
  @override
  def is_part_of_bst(self) -> bool:
    # add your complicated code here .....
    return something....
  ```

#### Testing

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

Note that this will run all tests, not just those for the `contains` method. To
restrict the tests to only that one, you could use:

```shell
python3 binary_tree_test.py BinaryTreeSearchPropertyTest
```

## Submission

Please submit your modified python files along with your analysis text file to
Canvas by the deadline.

