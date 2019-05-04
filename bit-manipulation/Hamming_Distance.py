# https://leetcode.com/problems/hamming-distance/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from queue import Queue
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


class Solution(object):
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    d = x ^ y
    print('d:', d, bin(d))

    ans = 0
    for k in range(0, 32):
      if (1 << k) > d:  # 1<<k 出现了两次 但这样的 for 循环用 while 循环更清晰
        break
      if d & (1 << k):
        ans += 1

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().hammingDistance(*args), end='\n-----\n')


  test(1, 4)
  test(3, 1)
else:
  print = lambda *args, **kwargs: None
