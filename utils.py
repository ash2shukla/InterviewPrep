from collections import namedtuple
from math import isnan

test = namedtuple('test', ['args', 'result'])

def do_test(tests, func):
    for args, result in tests:
        actual_result = func(None, *args)
        if type(actual_result) == float and isnan(result):
            assert isnan(actual_result), f'Expected nan but : actual {actual_result}'
        else:
            assert actual_result == result, f'Error: {args} Expected {result} : actual {actual_result}'
    else:
        print('all pass')