# https://leetcode.com/problems/search-a-2d-matrix-ii/
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


class Solution:
  def searchMatrix(self, matrix, target):
    if not matrix or not matrix[0]:
      return False
    r, c = 0, len(matrix[0]) - 1

    while r <= len(matrix) - 1 and c >= 0:
      print('r, c:', r, c)
      print('matrix[r][c], target:', matrix[r][c], target)
      if matrix[r][c] < target:
        r += 1  # 删去一行
      elif matrix[r][c] > target:
        c -= 1  # 删去一列
      else:
        return True

    return False


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().searchMatrix(*args), end='\n-----\n')


  test([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ], 5)
  test([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ], 20)
else:
  print = lambda *args, **kwargs: None
