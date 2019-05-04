# https://leetcode.com/problems/binary-number-with-alternating-bits/
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


class Solution(object):
  def hasAlternatingBits(self, n):
    """
    :type n: int
    :rtype: bool
    """
    bits = list(map(int, bin(n)[2:]))
    for i in range(len(bits) - 1):
      if not bits[i] ^ bits[i + 1]:
        return False

    return True

    # return reduce(lambda x, y: int(x)^int(y), bin(n)[2:])


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().hasAlternatingBits(*args), end='\n-----\n')


  test(5)
  test(7)
  test(11)
  test(10)
else:
  print = lambda *args, **kwargs: None
