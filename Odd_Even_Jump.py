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


# O(n^2)
# 找离i最近的A[j] >= A[i]
def findNearestLargeAndSmallJ(A):
  nearestLarge, nearestSmall = {}, {}
  length = len(A)
  for i in range(length):
    for j in range(i + 1, length):
      if i in nearestLarge and i in nearestSmall:
        break
      if A[i] <= A[j] and i not in nearestLarge:
        nearestLarge[i] = j
      if A[i] >= A[j] and i not in nearestSmall:
        nearestSmall[i] = j
  print('nearestLarge, nearestSmall:', nearestLarge, nearestSmall)
  return nearestLarge, nearestSmall


# O(n^2) maxn=2*10^4
# 性能瓶颈
# 找j > i, 且 A[j] 是大于 A[i] 的所有值中最小的
# tle
def findLargestAndSmallestJ(A):
  nearestLarge, nearestSmall = {}, {}
  length = len(A)
  for i in range(length):
    largeChoices = [(j, A[j]) for j in range(i + 1, length) if A[j] >= A[i]]
    smallChoices = [(j, A[j]) for j in range(i + 1, length) if A[j] <= A[i]]
    if largeChoices:
      nearestLarge[i] = min(largeChoices, key=itemgetter(1))[0]

    if smallChoices:
      nearestSmall[i] = max(smallChoices, key=itemgetter(1))[0]

  print('nearestLarge, nearestSmall:', nearestLarge, nearestSmall)
  return nearestLarge, nearestSmall


class Solution:
  def oddEvenJumps(self, A):  # -> int
    nearestLarge, nearestSmall = findLargestAndSmallestJ(A)
    # assert 0

    length = len(A)
    dp = {(length - 1, 0): True, (length - 1, 1): True}

    for i in range(length - 2, -1, -1):
      for j in range(0, 2):
        print('i, j:', i, j)

        if j == 0:
          if i not in nearestLarge:
            dp[(i, j)] = False
            continue
          k = nearestLarge[i]
          dp[(i, j)] = dp[(k, 1)]  # 跳到k

        else:  # 将进行偶数次跳
          if i not in nearestSmall:
            dp[(i, j)] = False
            continue
          k = nearestSmall[i]
          dp[(i, j)] = dp[(k, 0)]

    print('dp:', dp)
    return len(list(filter(bool, [dp[(i, 0)] for i in range(length)])))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().oddEvenJumps(*args), end='\n-----\n')


  test([10, 13, 12, 14, 15])
  test([2, 3, 1, 1, 4])
  test([5, 1, 3, 4, 2])
  test([1, 2, 3, 2, 1, 4, 4, 5])  # 0, 1, 2, 3, 4, 6, 7

else:
  print = lambda *args, **kwargs: None
