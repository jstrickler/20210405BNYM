#!/usr/bin/env python
import pytest

def test_two_plus_two_equals_four():  # <1>
    assert 2 + 2 == 4   #  <2>

if __name__ == '__main__':
    pytest.main([__file__, "-s"])