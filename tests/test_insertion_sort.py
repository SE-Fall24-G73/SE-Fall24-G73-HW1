import sys
import os

from myfile import insertionSort


def testcase_init_pass():
    array = [14, 12, 10, 8, 6, 4, 2, 0, -2]
    insertionSort(array)
    assert array == [-2, 0, 2, 4, 6, 8, 10, 12, 14]

def testcase_init_fail():
    array = [14, 12, 10, 8, 6, 4, 2, 0, -2]
    insertionSort(array)
    assert array == [-2, 0, 2, 4, 6, 8, 10, 14, 12]