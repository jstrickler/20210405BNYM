#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys

# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)
MAX_TRIES = 5

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    function1()

# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    pass


def function2(a, b):
    """
    This function does these things

    :param a: the thing
    :param b: the other thing
    :return: a value
    """

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()

# python spam.py mango apple 123
