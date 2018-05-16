def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_greater_than(a, b):
    assert a > b, "Expected {0} to be greater than {1} but this is not what we got".format(a, b)
    