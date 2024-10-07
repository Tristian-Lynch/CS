import random


def brute_force_mcss(seq):
    """
    Compute the maximum contiguous subsequence sum of a sequence of length n
    using the naive brute force algorithm.

    @param seq:     The sequence in question

    @return the maximum contiguous subsequence sum over seq.
    """

    sum = 0
    max_sum = 0
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            for k in range(i, j + 1):
                sum = sum + seq[k]
            if sum > max_sum:
                max_sum = sum
            sum = 0
    return max_sum


def better_brute_force_mcss(seq):
    """
    Compute the maximum contiguous subsequence sum of a sequence of length n
    using the slightly improved naive brute force algorithm.

    @param seq:     The sequence in question

    @return the maximum contiguous subsequence sum over seq.
    """

    max_sum = 0
    sum = 0
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            sum += seq[j]
            if sum > max_sum:
                max_sum = sum
        sum = 0
    return max_sum


def linear_mcss(seq):
    """
    Compute the maximum contiguous subsequence sum of a sequence of length n
    using the linear algorithm.

    @param seq:     The sequence in question

    @return the maximum contiguous subsequence sum over seq.
    """

    max_sum = 0
    running_sum = 0
    for i in range(len(seq)):
        running_sum += seq[i]
        if running_sum > max_sum:
            max_sum = running_sum
        elif running_sum < 0:
            running_sum = 0
    return max_sum


########################################################
# Helper functions
########################################################
def get_random_list(n):
    """
    Generate a random list of integers between -10000 and 10000.

    @param n:       The number of elements in the list to be generated.

    @warning This does not seed the random number generator, so don't expect
        true randomness.

    @return the randomly generated list.
    """
    return [random.randint(-10000, 10000) for i in range(n)]


class NotImplementYet(Exception):
    """
    Indicates that you have not yet implemented this method.
    """

    pass


if __name__ == "__main__":
    seq = get_random_list(10)
    bf_mcss_val = brute_force_mcss(seq)
    bbf_mcss_val = better_brute_force_mcss(seq)
    ln_mcsss_val = linear_mcss(seq)

    print(seq)
    print(f"Naive brute force computed a result of {bf_mcss_val}")
    print(f"Better brute foce computed a result of {bbf_mcss_val}")
    print(f"Linear computed a result of {ln_mcsss_val}")
