# https://leetcode.com/problems/convert-to-base-2/
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


class Solution:
  def baseNeg2(self, N):  # -> str
    if N == 0: return '0'
    n = N
    res = ''
    while n:
      part = (n % -2)
      if part < 0:
        part += 2
      res = str(part) + res
      n -= part
      # 整除一次
      n //= -2
    return res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().baseNeg2(*args), end='\n-----\n')


  test(2)
  test(3)
  test(4)
else:
  print = lambda *args, **kwargs: None
