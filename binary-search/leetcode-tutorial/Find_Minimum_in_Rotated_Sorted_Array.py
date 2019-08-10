# https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
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


def findPivot(nums):
  left, right = 0, len(nums) - 1
  leftMin, rightMax = nums[0], nums[-1]

  if leftMin < rightMax:
    return 0

  while left < right:
    mid = left + (right - left) // 2
    if nums[mid] >= leftMin:
      left = mid + 1
    else:
      right = mid
  return left


class Solution(object):
  def search(self, nums):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
      return -1

    left, right = None, None
    leftMin, rightMax = nums[0], nums[-1]
    if leftMin <= rightMax:  # 不分左右端
      return nums[0]
    else:
      return nums[findPivot(nums)]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().search(*args), end='\n-----\n')


  test([3, 4, 5, 1, 2])
  test([4, 5, 6, 7, 0, 1, 2])
else:
  print = lambda *args, **kwargs: None
