# https://leetcode.com/problems/bitwise-and-of-numbers-range/
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
  def rangeBitwiseAnd(self, m, n):  # -> int
    ans = 0
    for i in range(31, -1, -1):
      curM, curN = m & (1 << i), n & (1 << i)
      if curM == curN:
        ans |= curM
      else:
        break

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().rangeBitwiseAnd(*args), end='\n-----\n')


  test(5, 7)
  test(0, 1)
  test(11, 23)
  test(18, 23)

else:
  print = lambda *args, **kwargs: None
