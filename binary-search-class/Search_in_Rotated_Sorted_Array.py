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


def binarySearch(left, right, nums, target):
  if len(nums) == 0:
    return -1

  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1


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
  def search(self, nums, target):
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
      left, right = 0, len(nums) - 1
    else:
      pivot = findPivot(nums)
      if target >= nums[0]:  # >= 左端最小值  则target在左端
        left, right = 0, pivot - 1
      else:  # 否则在右端
        left, right = pivot, len(nums) - 1

    return binarySearch(left, right, nums, target)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().search(*args), end='\n-----\n')


  test([4, 5, 6, 7, 0, 1, 2], 0)
  test([4, 5, 6, 7, 0, 1, 2], 3)
  test([0, 1, 2, 4, 5, 6, 7], 3)
  test([1, 2, 4, 5, 6, 7, 0], 7)
  test([], 7)
  test([1], 1)
else:
  print = lambda *args, **kwargs: None
