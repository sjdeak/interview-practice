# https://leetcode.com/problems/utf-8-validation/
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
  def validUtf8(self, data):  # -> bool
    def isSingleByte(n):
      return n & (1 << 7) == 0

    def checkKByte(n, k):
      nonlocal timer
      checker = ((1 << k) - 1) << (8 - k)

      if checker & n == checker and 1 << (7 - k) & n == 0:
        return True
      else:
        return False

    one, two, three, four = 0b1, 192, 224, 240

    timer = 0
    for n in data:
      print('timer:', timer)

      if isSingleByte(n):
        if timer: return False
        continue

      if checkKByte(n, 1):
        if timer == 0: return False
        timer -= 1
        continue

      for k in range(4, 1, -1):
        print('n, k, checkKByte(n, k):', n, k, checkKByte(n, k))

        if checkKByte(n, k):
          if timer: return False
          timer += k - 1
          break
      else:
        return False

    return timer == 0


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().validUtf8(*args), end='\n-----\n')


  test([197, 130, 1])
  test([235, 140, 4])
  test([248, 130, 130, 130])
else:
  print = lambda *args, **kwargs: None
