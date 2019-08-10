# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/
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
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


def binarySearch(left, right, target):
  while left <= right:
    mid = right - (right - left) // 2

    if mid ** 2 == target:
      return mid

    if mid ** 2 > target:
      right = mid - 1
    else:
      left = mid + 1

  return -1


class Solution(object):
  def isPerfectSquare(self, num):
    return binarySearch(0, num, num) != -1


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().isPerfectSquare(*args), end='\n-----\n')


  test(16)
  test(14)
  test(1)
else:
  print = lambda *args, **kwargs: None
