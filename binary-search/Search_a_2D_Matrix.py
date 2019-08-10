# https://leetcode.com/problems/search-a-2d-matrix/
import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy

sys.setrecursionlimit(1000000)


def binarySearch(mat, x):
  getA = lambda idx: mat[idx // len(mat[0])][idx % len(mat[0])]

  left, right = 0, len(mat) * len(mat[0]) - 1

  while left <= right:
    mid = left + (right - left) // 2

    if getA(mid) > x:
      right = mid - 1
    elif getA(mid) < x:
      left = mid + 1
    else:
      return mid

  return -1


class Solution:
  def searchMatrix(self, matrix, target):  # -> bool
    if not matrix or not matrix[0]:
      return False
    return binarySearch(matrix, target) != -1


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().searchMatrix(*args), end='\n-----\n')


  #   test([
  #   [1,   3,  5,  7],
  #   [10, 11, 16, 20],
  #   [23, 30, 34, 50]
  # ], 3)
  #   test([
  #   [1,   3,  5,  7],
  #   [10, 11, 16, 20],
  #   [23, 30, 34, 50]
  # ], 13)
  #   test([], 1)
  #   test([[]], 1)
  #   test([[1],[3]], 0)
  #   test([[1],[3]], 1)
  test([[1], [1]], 2)
else:
  print = lambda *args, **kwargs: None
