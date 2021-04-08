#!/usr/bin/env python
from collections import namedtuple
import pytest

Person = namedtuple('Person', 'first_name last_name')  # <1>

FIRST_NAME = "Guido"
LAST_NAME = "Von Rossum"

@pytest.fixture  # <2>
def person():
    """
    Return a 'Person' named tuple with fields 'first_name' and 'last_name'
    """
    return Person(FIRST_NAME, LAST_NAME)  # <3>


def test_first_name(person):  # <4>
    assert person.first_name == FIRST_NAME

def test_last_name(person):  # <4>
    assert person.last_name == LAST_NAME

@pytest.fixture
def expected():
    return 4

@pytest.fixture
def animal():
    return 'wombat'

def test_two_plus_two_is_four(expected, animal):
    assert 2 + 2 == expected
    assert animal == 'wombat'



