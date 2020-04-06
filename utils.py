from collections import namedtuple
from math import isnan
import unittest


test = namedtuple('test', ['args', 'result'])

def flatten(list_of_lists):
    flat_lst = []
    for lst in list_of_lists:
        flat_lst.extend(lst)
    return sorted(flat_lst)

def do_test(tests, func):
    for args, result in tests:
        actual_result = func(None, *args)

        if type(actual_result) == float and isnan(result):
            assert isnan(actual_result), f'Expected nan but : actual {actual_result}'
        elif type(actual_result) == list:
            flat_actual = flatten(actual_result)
            flat_result = flatten(result)
            unittest.TestCase().assertListEqual(flat_actual, flat_result), f'Error: {args} Expected {result} : actual {actual_result}'
        else:
            assert actual_result == result, f'Error: {args} Expected {result} : actual {actual_result}'
    else:
        print('all pass')