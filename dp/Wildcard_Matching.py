# https://leetcode.com/problems/wildcard-matching/
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
  def isMatch(self, s, p):  # -> bool
    # @dump_args
    @lru_cache(None)
    def dp(i, j):
      if j < 0:
        return False
      if i < 0:
        return p[:j + 1] == '*' * (j + 1)

      if j == 0:
        if p[j] == '*':
          return True
        elif p[j] == '?':
          return i == 0
        else:
          return i == 0 and s[0] == p[0]

      # 此处保证 i >= 0, j > 0
      if p[j] == '*':
        # return any([dp(ni, j-1) for ni in range(i+1)])
        return dp(i - 1, j) or dp(i, j - 1)  # 转移优化的关键一步: 只做最小的一步转移
      elif p[j] == '?':
        return dp(i - 1, j - 1)
      else:
        if s[i] == p[j]:
          return dp(i - 1, j - 1)
        else:
          return False

    if not p:
      return not s
    else:
      return dp(len(s) - 1, len(p) - 1)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().isMatch(*args), end='\n-----\n')


  test("aa", "a")
  test("aa", "*")
  test("cb", "?a")
  test("adceb", "*a*b")
  test("acdcb", "a*c?b")
  test("", "")
  test("ho", "**ho")
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
