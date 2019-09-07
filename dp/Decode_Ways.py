# https://leetcode.com/problems/decode-ways/
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

"""
严格按照转移方程实现，做最小的一步转移，不要多考虑其他的东西
题面中不存在合法不合法的问题，只是统计解的数目   "不合法" 其实就是解的数目为0
"""


class Solution:
  @lru_cache(None)
  def numDecodings(self, s):  # -> int
    # len <= 1时边界处理
    if s == '0':
      return 0
    if len(s) <= 1:
      return 1

    res = 0
    if s[-1] != '0':
      res += self.numDecodings(s[:-1])

    if 10 <= int(s[-2:]) <= 26:
      res += self.numDecodings(s[:-2])

    return res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().numDecodings(*args), end='\n-----\n')


  test("12")
  test("226")
  test("0")
  test("100")
  test("1010")
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
