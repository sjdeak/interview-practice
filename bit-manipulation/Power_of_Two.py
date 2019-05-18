# https://leetcode.com/problems/power-of-two/
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
  def isPowerOfTwo(self, n):  # -> bool
    if n == 0:
      return False
    return bool(not n & (n - 1))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().isPowerOfTwo(*args), end='\n-----\n')


  test(0)
  test(1)
  test(16)
  test(218)
else:
  print = lambda *args, **kwargs: None
