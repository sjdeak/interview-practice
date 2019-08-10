# https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/
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


def refreshGlobals():
  pass


refreshGlobals()


# The guess API is already defined for you.
#  num, your guess
#  -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
  def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 1, n
    while left <= right:
      mid = left + (right - left) // 2
      if guess(mid) == 0:
        return mid
      elif guess(mid) == 1:
        left = mid + 1
      else:
        right = mid - 1


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().guessNumber(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
