# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


class Solution:
  def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    mask = 0
    for i in range(32, -1, -1):
      mask |= (1 << i)  # 100000 110000 111000...
      set_ = set()
      for num in nums:
        set_.add(num & mask)
      cand = ans | (1 << i)
      for prefix in set_:
        if cand ^ prefix in set_:
          ans = cand  # p0 p1 ... pi 1
          break
        else:
          pass  # ans = p0 p1 ... pi 0
    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findMaximumXOR(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
