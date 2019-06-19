# https://leetcode.com/contest/leetcode-weekly-contest-34/problems/range-addition-ii/
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


class Solution:
  def maxCount(self, m, n, ops):  # -> int
    resA, resB = m, n
    for (a, b) in ops:
      resA = min(resA, a)
      resB = min(resB, b)

    return resA * resB


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxCount(*args), end='\n-----\n')


  test(3, 3, [[2, 2], [3, 3]])
  test(3, 3, [])
else:
  print = lambda *args, **kwargs: None
