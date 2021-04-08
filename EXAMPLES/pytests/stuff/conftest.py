#!/usr/bin/env python
from pytest import fixture

@fixture
def common_fixture():  # <1>
    """
    Return a silly data string

    :return:
    """
    return "DATA"

@fixture
def animal():
    """
    Return my favorite animal name.

    :return:
    """
    return "wombat"


def pytest_runtest_setup(item):  # <2>
    print("YOUR HAIR IS ON FIRE!!!,", item)
