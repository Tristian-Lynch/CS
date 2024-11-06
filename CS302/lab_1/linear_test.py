from mcss import linear_mcss

def test_positive_numbers():
    assert linear_mcss([1, 2, 3, 4]) == 10

def test_negative_numbers():
    assert linear_mcss([-1, -2, -3, -4]) == -1

def test_mixed_numbers():
    assert linear_mcss([1, -2, 3, 4, -1, 2]) == 8

def test_single_element():
    assert linear_mcss([9]) == 9

def test_empty_sequence():
    assert linear_mcss([]) == 0
