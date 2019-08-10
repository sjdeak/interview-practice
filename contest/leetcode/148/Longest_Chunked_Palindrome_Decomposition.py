# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
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
  def longestDecomposition(self, text):  # -> int

    @lru_cache(None)
    def dp(i, j):
      if i > j:
        return 0
      if i == j:
        return 1

      res = 1
      k = 0
      while i + k < j - k:
        if text[i:i + k + 1] == text[j - k:j + 1]:
          res = max(res, 2 + dp(i + k + 1, j - k - 1))
        k += 1

      return res

    return dp(0, len(text) - 1)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().longestDecomposition(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
