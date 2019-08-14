# https://leetcode.com/problems/regular-expression-matching/
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
    @dump_args
    @lru_cache(None)
    def dp(i, j):
      if j < 0:
        return i < 0

      # 此处保证 j >= 0
      if p[j] == '*':
        if i >= 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):
          return dp(i, j - 2) or dp(i - 1, j)
        else:
          return dp(i, j - 2)

      elif p[j] == '.':
        if i >= 0:
          return dp(i - 1, j - 1)
        else:
          return False

      else:
        if i >= 0 and s[i] == p[j]:
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


  # test("aa", "a")
  # test("aa", "a*")
  # test("ab", ".*")
  # test("aab", "c*a*b")
  # # test("acdcb", "a*c?b")
  # test("mississippi", "mis*is*p*.")

  test("a", ".*..a*")

else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
