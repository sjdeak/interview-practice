# https://leetcode.com/problems/ugly-number-ii/description/
import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import *
from copy import deepcopy

sys.setrecursionlimit(1000000)


class Solution:
  def nthUglyNumber(self, N):  # -> int
    if N == 1:
      return 1

    choices = [2, 3, 5]
    now = 1
    for n in range(2, N + 1):
      now = min(choices)
      del choices[choices.index(now)]
      for c in [2 * now, 3 * now, 5 * now]:
        if c not in choices:
          insort(choices, c)

      choices = choices[:100]
      print('n, now, choices:', n, now, choices)

    return now


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().nthUglyNumber(*args), end='\n-----\n')


  test(10)
  test(1)
else:
  print = lambda *args, **kwargs: None
