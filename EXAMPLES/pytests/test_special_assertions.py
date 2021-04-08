#!/usr/bin/env python
import pytest
import math

FILE_NAME = 'IDONOTEXIST.txt'

def test_missing_filename():
    with pytest.raises(FileNotFoundError):  # <1>
        open(FILE_NAME)  # <2>

def test_list():
    print()
    value = .1 + .2  # some calculation that expects .3 as the answer
    expected = .3
    assert value == pytest.approx(expected)  # <3>

def test_approximate_pi():
    value = 22 / 7
    expected = math.pi
    tolerance = .001  # default .000001

    assert value == pytest.approx(expected, tolerance)  # <4>

