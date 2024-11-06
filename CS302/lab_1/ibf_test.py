from mcss import better_brute_force_mcss

def test_positive_numbers():
    assert better_brute_force_mcss([1, 2, 3, 4]) == 10

def test_negative_numbers():
    assert better_brute_force_mcss([-1, -2, -3, -4]) == -1

def test_mixed_numbers():
    assert better_brute_force_mcss([1, -2, 3, 4, -1, 2]) == 8

def test_single_element():
    assert better_brute_force_mcss([9]) == 9

def test_empty_sequence():
    assert better_brute_force_mcss([]) == 0
