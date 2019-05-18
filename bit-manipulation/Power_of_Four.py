# https://leetcode.com/problems/power-of-four/
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
  def isPowerOfFour(self, num):  # -> bool
    if num & (num - 1):
      return False
    return bool(num.bit_length() % 2)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().isPowerOfFour(*args), end='\n-----\n')


  test(16)
  test(5)
  test(64)
  test(0)
  test(1)
else:
  print = lambda *args, **kwargs: None
