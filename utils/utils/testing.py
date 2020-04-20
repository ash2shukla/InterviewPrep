from collections import namedtuple
from math import isnan
from utils.linked_list import ListNode
import unittest
from utils.bin_tree import TreeNode, treenode
from typing import List
from types import FunctionType, MethodType


test = namedtuple('test', ['args', 'result'])


def assertEqualBinTrees(tree1: List[treenode] , tree2: List[treenode]):
        assert len(tree1) == len(tree2), "Number of nodes are not same in trees."
        for n1, n2 in zip(tree1, tree2):
            assert n1.value == n2.value, f"Node values mismatch {n1, n2}"
            assert n1.parent_index == n2.parent_index, f"Node parents mismatch {n1, n2}"
            assert n1.alignment == n2.alignment, f"Node alignment mismatch {n1, n2}"


def flatten(list_of_lists):
    flat_lst = []
    for lst in list_of_lists:
        flat_lst.extend(lst)
    return sorted(flat_lst)


def do_test(tests, func):
    for args, result in tests:
        if isinstance(func, FunctionType):
            actual_result = func(None, *args)
        elif isinstance(func, MethodType):
            actual_result = func(*args)

        if type(actual_result) == float and isnan(result):
            assert isnan(actual_result), f'Expected nan but : actual {actual_result}'
        elif isinstance(actual_result, list) and all(type(i) == list for i in actual_result):
            flat_actual = flatten(actual_result)
            flat_result = flatten(result)
            unittest.TestCase().assertListEqual(flat_actual, flat_result), f'Error: {args} Expected {result} : actual {actual_result}'
        elif isinstance(actual_result, ListNode):
            unittest.TestCase().assertListEqual(list(actual_result), result), f'Error: {args} Expected {result} : actual {list(actual_result)}'
        elif isinstance(actual_result, TreeNode):
            assertEqualBinTrees(list(actual_result), result)
        else:
            assert actual_result == result, f'Error: {args} Expected {result} : actual {actual_result}'
    else:
        print('all pass')


