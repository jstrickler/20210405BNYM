#!/usr/bin/env python
import pytest

# subject under test
def triple(x):  # <1>
    return x * 3

# actual test
test_data = [(5, 15), ('a', 'aaa'), ([True], [True, True, True]), (0,0), (False, False)]  # <2>

@pytest.mark.parametrize("input,expected", test_data)  # <3>
def test_triple(input, expected):  # <4>
    # print("input {} result {}:".format(input, expected))  # <4>
    assert triple(input) == expected   # <5>


if __name__ == "__main__":
    pytest.main([__file__, '-s'])

