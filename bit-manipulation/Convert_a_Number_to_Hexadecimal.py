# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
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
  def toHex(self, num):  # -> str
    chMap = list('0123456789abcdef')
    if num == 0:
      return "0"
    if num < 0:
      num = num + (1 << 32)
    print('bin(num):', bin(num))
    ans = ''
    while num:
      print('in loop num:', num)
      tailNum = ((1 << 4) - 1) & num
      ans = chMap[tailNum] + ans
      num >>= 4

    print('ans:', ans)
    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().toHex(*args), end='\n-----\n')


  test(26)
  test(33)
  test(1)
  test(0)
  test(-1)
else:
  print = lambda *args, **kwargs: None
