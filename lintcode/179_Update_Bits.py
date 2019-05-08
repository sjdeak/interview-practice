# https://www.lintcode.com/problem/update-bits/description
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from queue import Queue
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


class Solution:
  """
   n: An integer
   m: An integer
   i: A bit position
   j: A bit position
  : An integer
  """

  def updateBits(self, n, m, i, j):
    if n < 0: n = n + (1 << 32)
    if m < 0: m = m + (1 << 32)

    lenM = j - i + 1
    partN = n & (((1 << lenM) - 1) << i)
    m = m << i

    ans = n ^ m ^ partN

    if (1 << 31) & ans:  # ans为负数时 手工把补码转成十进制
      ans = (((1 << 31) - 1) & ans) - (1 << 31)

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().updateBits(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
