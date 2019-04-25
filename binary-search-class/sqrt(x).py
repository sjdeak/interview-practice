# https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
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


def binarySearch(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :type check: function 判断是否找到
  :rtype: int
  """
  if len(nums) == 0:
    return -1

  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    # if check(mid, target):
    if mid ** 2 <= target <= (mid + 1) ** 2:
      return mid
    elif mid ** 2 < target:
      left = mid + 1
    else:
      right = mid - 1

  # End Condition: left > right
  return -1


def check(i, target):
  return i ** 2 <= target <= (i + 1) ** 2


class Solution:
  def mySqrt(self, x):  # -> int
    # todo MLE
    return binarySearch(list(range(x + 1)), x)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().mySqrt(*args), end='\n-----\n')


  test(8)
  test(2)
else:
  print = lambda *args, **kwargs: None

"""
left, right
A[mid] == target
"""
