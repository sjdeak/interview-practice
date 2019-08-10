# https://leetcode.com/problems/find-the-duplicate-number/
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
  def findDuplicate(self, A):  # -> int
    A.sort()
    for i, n in enumerate(A[:-1]):
      if A[i] == A[i + 1]:
        return A[i]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findDuplicate(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
