# CS302: Lab Assignment 1: Exploring MCSS and Asymptotic Analysis

## Learning Objectives

At the end of the this lab, you should be able to:

1. Implement different solutions to the maximum contiguous subsequence sum
   problem.

2. Explore the impact of each solution on the runtime of the program, in light
   of the discussion about asymptotic analysis.

## Setup

For this lab, you will need to a have a version of `python3` installed. In
addition, you will need to have the `matplotlib` library installed so you could
visualize the runtime of each solution. The easiest way to do so is to grab a
terminal window (or PowerShell on Windows) and enter the following command:

```shell
pip install matplotlib
```

Alternative, if `pip` not installed, you can use:

```shell
python -m pip install matplotlib
```

You can also run the whole lab in an IDE. I walk you through a possible setup
using VisualStudioCode in a video on the Canvas page.

## Implementing MCSS

All of the code you have to implement lives in the `mcss.py` file. In there,
you will find three documented functions that you should implement. Each has a
`TODO` label for where to add your code.

### Brute Force MCSS

In the first step, you should implement the naive brute force algorithm for
finding an MCSS in an input array. You should add your code to the
`brute_force_mcss` function in `mcss.py`.

To test if your code works, I have provided you with a set of unit tests that
can be found in `bf_test.py`. If you prefer to run things from a terminal
window, you can run those through:

```shell
pytest bf_test.py
```

Initially, all tests will fail with a not implemented exception. As you write
your code, the test cases will start giving more meaningful information. Feel
free to inspect the test cases for information about each one.

### Better Brute Force

Next, you should implement the O(n^2) brute force algorithm for MCSS in the
`better_brute_force` function (make sure to remove the `raise NotImplementYet`)
line after adding your code.

Similarly, you can test your code by running the test cases in the
`ibf_test.py` file.

### Linear MCSS

Finally, you should implement the linear version of the MCSS algorithm in the
`linear_mcss` function. Again, you can test your code once done by running the
test cases in `linear_test.py`.

### Visualizing Behavior

To visualize the behavior of each implementation as the size of the array grows
large, I have provided you with a simple "MCSS racing" program in `racing.py`.
After you have implemented all three of the approaches, you can run this
program and it will plot the runtime of each approach as the size of the array
increases. You can run it as follows (if from a terminal):

```shell
python racing.py
```

**Running this will take a bit of time as the brute force algorithm is indeed
very slow**. Once it is done, you should see a few plots show up that visualize
the runtime of each algorithm as a function of the size of the input array.
Feel free to inspect the code in `racing.py` for further information.

### Submission

In addition to `mcss.py`, please record your observations about the plot in the
last step in the file `observations.txt` and submit both of these files to the
Canvas drop box by the deadline.

