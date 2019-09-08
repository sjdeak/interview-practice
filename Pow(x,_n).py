# https://leetcode.com/problems/powx-n/
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
  # template 快速幂
  def myPow(self, x, n):  # -> float
    res = 1
    p = x
    t = abs(n)
    bitLen = len(bin(t)[2:])
    while t:
      # print('k, res, p, bin(absN):', k, res, p, bin(t))
      if t & 1:
        res *= p
      p *= p
      t >>= 1 # 位运算真的很酷

    return 1 / res if n < 0 else res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().myPow(*args), end='\n-----\n')


  test(2.00000, 10)
  test(2.10000, 3)
  test(2.00000, -2)
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
