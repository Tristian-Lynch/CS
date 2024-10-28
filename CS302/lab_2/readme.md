# CS302: Lab Assignment 1: Exploring MCSS and Asymptotic Analysis

## Learning Objectives

At the end of the this lab, you should be able to:

1. Implement a queue using different approaches for the underlying data
   structure.

2. Solve a real problem using the stack data structure.

3. Analyze your proposed solution and compare their advantages and
   disadvantages.

## Setup

For this lab, you will need to a have a version of `python3` installed. In
addition, you will need to have the `unittest` library installed so you could
run the unit tests provided for each problem.The easiest way to do so is to
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

## Problem 1: Exploring a queue

In this first problem, we would like to implement a queue using two different
underlying data structures: (1) a circular array and (2) two stacks. For each
one of those possibilities, you should implement four methods:

1. `enqueue`: Takes as argument an item and adds it to the queue.

2. `dequeue`: Remove the top (or head) of the queue and returns it to the user.

3. `peek`: **Read** the top of the queue and return it to the user, but do not
   remove it from the queue.

4. `__str__`: Returns a string representation of the current status of
   underlying data structure of the queue.

### Implementing a queue using a circular array

First, we would like to implement a queue using a circular array. A circular
array (or list) is an array **of fixed size** but for which elements can rotate
once it is full. In other words, when an element is remove from this array, it
does not actually remove it, it only allows new elements to take its place.
In this step, you will modify the four methods above in the `circular_queue.py`
file.

Here is an example. Consider a situation where a queue is implemented as a
circular array of fixed size 3 (i.e., we can at most hold three elements in the
queue). Initially, the array contains invalid values, you could use `None` for
these.

1. Initially, our queue is `[None, None, None]`.

2. Now assume we do the following: `enqueue(1)`, then our array becomes `[1,
   None, None]`.

3. Next assume we `enqueue(2)` and `enqueue(3)`, then our array becomes `[1, 2,
   3]`.

4. If we try to `enqueue` anything further, we should raise an exception as our
   queue is full.

5. Now here's the trick, if I call `dequeue()`, then my queue will pop the top
   element, which is `1` in this case. However, our inner array will still look
   like `[1, 2, 3]`, except that our queue now somehow knows that the top of
   the queue is `2` and that the spot that contained the `1` is free to be
   reused.

6. Assume now we do `enqueue(4)`, then the queue add the `4` __in the spot that
   was previously used by 1__, and thus our array looks like `[4, 2, 3]`.
   *But* our queue still knows that `2` is at the top of the queue and `4` is
   at the tail of the queue.

I encourage to take a few more examples to truly wrap your head around this
implementation.

#### Hints

You can clearly see from the example that the queue data structure needs to
know where its top element is (we call this `head`), where its last element is
(we call this `tail`), and for simplicity, its current size (or number of
active elements). As a challenge, consider remove the `size` attribute and
implementing the queue using only `head` and `tail`.

Feel free to add as many attributes as you need to the `CircularArrayQueue`
class, but please do not change anything in the `IQueue` abstract class.

#### Testing

I strongly recommend that you develop incrementally. In other words, write your
`enqueue` method and make sure your `enqueue` tests pass before you move on to
the `dequeue` method and so on.

To run the tests, if you are using an IDE, then you can use the IDE appropriate
method for running individual tests.

If you are using a terminal, then you can run all tests using:

```shell
python3 circular_queue_test.py
```

or,

```shell
python circular_queue_test.py
```

depending on your `python` installation.

To run a single test from the command line, you can use the following:

```shell
python3 circular_queue_test.py CircularArrayQueueTest.test_enqueue_size
```

This will only run the `test_enqueue_size` test from the all the tests. You can
then replace that with the specific test you'd like to run based on the method
you are working on.

### Implementing a queue using two stacks

As an alternative to the circular array implementation, one could use two
stacks to implement a queue. In this part, we would like to do exactly that.

I have provided you with an implementation of a stack that you can find in
`stack.py`. There is really nothing fancy about it except that it implements
`push` and `pop`. Please refer to the examples in the documentation of that
class for more information.

In this part, you will implement the four methods in the `stacks_queue.py`
file.

#### Hints

Unlike the circular array implementation, this approach shifts the complexity
of the implementation to the `dequeue` and `peek` methods rather than the
`enqueue` method.

Additionally, it is okay if in this implementation, a lot of data keeps moving
back and forth between the two stacks. First, focus on correctness of your
implementation and do not try to optimize before having a correct solution.

#### Testing

Again, I strongly encourage you to follow an incremental approach to
implementing this problem. You can run your test cases in a very similar way to
the first part of this problem, except you'll replace `circular_queue_test.py`
with `stacks_queue_test.py` if running from the terminal. If using your IDE,
then you simply have to click on the correct tab.

## Problem 2: Writing an arithmetic postfix evaluator

For us humans, we are used to writing and evaluating arithmetic expressions
using a well-known precedence ordering and parenthesis. For example, we all
know that `(2 + 3) * 2` is 10 while `2 + 3 * 2` is 8. This representation of
arithmetic expressions is referred to as the _infix_ notation.

However, programming languages have no notion of precedence when evaluating
arithmetic expressions. They thus use a different representation of such
expressions, one that is referred to as the _postfix_ notation.

In the postfix notation, the operator (say, addition) is written **after** the
operands. For examples, to add 2 and 3, we write `2 3 +` in postfix notation.
There are two clear advantages for such a notation:

1. The order of the operation is unambiguous without needed parenthesis. Here
   are some examples to make it clear:
   - `2 + 3` is written as `2 3 +`.
   - `2 + 3 * 2` is written as `2 3 2 * +`. In this format, your computer will
     always evaluate `3 * 2` first and then apply the `2 + answer` to its
     outcome. No need for parenthesis!
   - Alternatively, `(2 + 3) * 2` is written as `2 3 + 2 *` in postfix. Here,
     the computer will first evaluate `2 3 +` giving us 5, which makes the
     expression become `5 2 *` which produces our desired `10`.
   - Here's one more example, `2 * (3 - 1)` is written as `2 3 1 - *` in
     postfix. Alternatively, `2 * 3 - 1` is written as `2 3 * 1 -`.

2. A computer can very easily evaluate an expression in postfix notation using
   a stack.

Your job in this problem is write a postfix expression evaluator. Given a
expression in postfix notation, your evaluator will employ an algorithm of your
design to evaluate the expression.

First, please read through the documentation in the `postfix.py` source code in
`problem2/`. Your job is to only implement the `evaluate_expr` method. You can
also use the `Stack` class that I have provided for you in the `stack.py` file
(It has already been imported for you, so you can use it directly).

Here is a simple breakdown of a solution. Reading through the expression, you
can keep pushing operands onto a stack. Once you encounter an operator, you
_pop_ two elements from the stack, apply the operator to them, then push the
result back onto the stack. Then rinse and repeat as long as you have more
operands and operators in the expression. You can see the clear advantage here
since your really do not have to worry about any precedence in the operators,
you get that for free from the postfix notation.

**Please** do take a few examples before you attempt to write a solution, then
go ahead and implement your design.

### Handling malformed expressions

In addition to evaluating an expression, your evaluator should also be able to
catch malformed expressions. Surprisingly, that is very easy without doing any
sort of analysis on the expression, it will naturally flow with the algorithm
describe above.

For example, consider the expression `2 3 + -`. This is clearly malformed since
there is an extra operator (the `-`) there. Your implementation should detect
such errors while trying to evaluate the expression. _Please_ refrain from
scanning the entire expression and matching each operator with two operands,
that is way to complicated with something that can be done normally in one line
of code :)

As always, take a few examples, note what your algorithm should do when you see
such cases, and ask me questions as you go along.

### Helper functions

I provide you with some helper methods and attributes in the `PostfixEvaluator`
class, please do read the documentation for those before starting to write your
code.

### Testing

Testing for this problem will follow the same approach as for problem 1. First,
you should focus on writing the algorithm that would evaluate well-formed
expressions and pass the tests for those. Then you can move on to finally
adding the error checking conditions (which are not many and easily detectable,
please don't spend more than 15 minutes on this!).

To run the test cases from the terminal, you can again use:

```shell
python3 postfix_tests.py
```

If you are running in VisualStudioCode, then please edit the `settings.json`
file under `.vscode/` and change `problem1` to `problem2` so you can run the
test cases for this specific problem. Otherwise, only tests for problem 1 will
show up.

## Problem 3: Analyzing your solutions

Lastly, we would like to analyze the runtime of your proposed solutions. Please
answer the questions in `problem3.txt` about each of problem 1 and problem 2.
_You do not have to prove your asymptotic analysis_, you only should state it.

**You can assume that all stack operations are O(1)**, even though they're
really not in my stupid implementation!

## Submission

Please submit your modified python files along with your analysis text file to
Canvas by the deadline.

