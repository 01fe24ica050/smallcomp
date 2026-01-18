def smallest_largest(a, b, c):
    return min(a, b, c), max(a, b, c)

def test_smallest_largest():
    assert smallest_largest(3, 7, 1) == (1, 7)