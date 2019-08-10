# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/
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


class Solution(object):
  def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    if length < 2:
      return nums.index(max(nums))

    left, right = 0, length - 1
    while left + 1 <= right:
      mid = left + (right - left) // 2
      # print('left, mid, right:', left, mid, right)

      # 这种实现找到的Peak是偏右的
      # 如果是mid和mid-1比较，找到的Peak就会偏左
      if nums[mid] > nums[mid + 1]:
        right = mid
      else:
        left = mid + 1

    return left if nums[left] > nums[right] else right


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findPeakElement(*args), end='\n-----\n')


  test([1, 2])
  test([1, 2, 3, 1])
  test([1, 2, 1, 3, 5, 6, 4])
else:
  print = lambda *args, **kwargs: None
