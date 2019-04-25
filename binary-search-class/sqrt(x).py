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


def binarySearch(left, right, target):
  while left <= right:
    mid = (left + right) // 2
    if mid ** 2 <= target <= (mid + 1) ** 2:
      return mid
    elif mid ** 2 < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1


class Solution:
  def mySqrt(self, x):  # -> int
    if x == 1:
      return 1

    return binarySearch(0, x, x)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().mySqrt(*args), end='\n-----\n')


  test(8)
  test(2)
  test(0)
  test(1)
else:
  print = lambda *args, **kwargs: None

# todo
""" 如何写出通用的二分查找模板?
left, right
A[mid] == target
"""
