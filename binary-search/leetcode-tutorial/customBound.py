# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/
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


# 明确要找什么: >tar 的第一个下标
def customBound(A, target):
  print('A, target:', A, target)
  length = len(A)
  left, right = 0, length - 1
  while left < right:  # 循环不变式保证ans必在[left, right]中
    mid = left + (right - left) // 2  # 使得mid往左偏 通过与下述判断语句配合 保证 A中只有两个元素时经过循环A仍然会继续变小
    if A[mid] > target:
      right = mid
    elif A[mid] <= target:
      left = mid + 1

  return left


class Solution:
  def nextGreatestLetter(self, letters, target):  # -> str
    nums = list(map(ord, letters))
    target = ord(target)
    ansI = customBound(nums, target)
    ans = letters[ansI]
    if ansI == len(letters) - 1 and not ord(ans) > target:
      ans = letters[0]
    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().nextGreatestLetter(*args), end='\n-----\n')


  test(["c", "f", "j"], 'a')
  test(["c", "f", "j"], 'c')
  test(["c", "f", "j"], 'd')
  test(["c", "f", "j"], 'g')
  test(["c", "f", "j"], 'j')
  test(["c", "f", "j"], 'k')
else:
  print = lambda *args, **kwargs: None
