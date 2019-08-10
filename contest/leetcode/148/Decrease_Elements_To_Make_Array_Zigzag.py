# https://leetcode.com/contest/weekly-contest-148/problems/decrease-elements-to-make-array-zigzag/
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


def solve(A, kind):
  def condition():
    if kind == 'even':
      return i % 2
    else:
      return not i % 2

  cnt = 0
  for i, n in enumerate(A[:-1]):
    print('i, cnt:', i, cnt)
    if condition():  # kind = 'even', i = 1
      if A[i] >= A[i + 1]:
        cnt += A[i] - (A[i + 1] - 1)
        A[i] = A[i + 1] - 1
    else:  # i = 0
      if A[i] <= A[i + 1]:
        cnt += A[i + 1] - (A[i] - 1)
        A[i + 1] = A[i] - 1

  print('kind, zigzag A:', kind, A)
  return cnt


class Solution:
  def movesToMakeZigzag(self, nums: list):  # -> int
    return min(solve(nums.copy(), 'even'), solve(nums.copy(), 'odd'))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().movesToMakeZigzag(*args), end='\n-----\n')


  test([1, 2, 3])
  test([9, 6, 1, 6, 2])
  test([7, 4, 8, 9, 7, 7, 5])
  test([10, 4, 4, 10, 10, 6, 2, 3])
else:
  print = lambda *args, **kwargs: None
