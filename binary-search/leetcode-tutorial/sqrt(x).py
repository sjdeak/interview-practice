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


# 其实是要找upper_bound
def binarySearch(left, right, target):
  while left < right:
    mid = right - (right - left) // 2
    if mid ** 2 > target:
      right = mid - 1
    else:
      left = mid
  return left


class Solution:
  def mySqrt(self, x):  # -> int
    return binarySearch(0, x, x)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().mySqrt(*args), end='\n-----\n')


  test(8)
  test(2)
  test(9)
  test(0)
  test(1)
else:
  print = lambda *args, **kwargs: None

# todo
""" 如何写出通用的二分查找模板?
left, right
A[mid] == target
"""
