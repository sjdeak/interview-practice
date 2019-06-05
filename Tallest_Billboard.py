# https://leetcode.com/problems/tallest-billboard/solution/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


class Solution:
  def tallestBillboard(self, rods):  # -> int
    @lru_cache(None)
    def dp(i, s):
      if i == len(rods):
        return 0 if s == 0 else -inf
      return max([dp(i + 1, s), dp(i + 1, s + rods[i]) + rods[i], dp(i + 1, s - rods[i])])

    return dp(0, 0)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().tallestBillboard(*args), end='\n-----\n')


  test([1, 2, 3, 6])
  test([1, 2, 3, 4, 5, 6])
  test([1, 2])
else:
  print = lambda *args, **kwargs: None
