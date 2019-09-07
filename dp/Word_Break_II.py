# https://leetcode.com/problems/word-break-ii/
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
在word break的基础上要求输出所有解

用dfs直接做是可以，但效率会不会没有dp的做法好?
dp 输出所有解 很长时间没写了 
"""


class Solution:
  def wordBreak(self, s, wordDict):  # -> List[str]

    pass


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().wordBreak(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
