# https://leetcode.com/contest/weekly-contest-135/problems/minimum-score-triangulation-of-polygon/
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


def getValue(A, indexes):
  return reduce(lambda x, y: x * y,
                map(lambda i: A[i], indexes))


def getAdditionalTriangle(nowS, i):
  """
  计算新增下标为i的节点后，增加的value
  """
  s = bin(nowS)[2:]
  i = len(s) - 1 - i
  adjacents = []
  for k in range(1, 50 + 1):
    li, ri = i - k, i + k
    if li in range(len(s)) and s[li] == '1':
      adjacents.append(li)
    if len(adjacents) == 2:
      break
    if ri in range(len(s)) and s[ri] == '1':
      adjacents.append(ri)
    if len(adjacents) == 2:
      break

  return adjacents + [i]


class Solution:
  def minScoreTriangulation(self, A):  # -> int
    length = len(A)
    dp = defaultdict(lambda: float('inf'))

    queues = [deque() for _ in range(length + 1)]
    for perm in permutations('1' * 3 + '0' * (length - 3)):
      value = getValue(A, tuple((i for i, ch in enumerate(perm) if ch == '1')))
      s = int('0b' + ''.join(perm), 2)
      dp[s, 1] = value
      queues[1].append((s, 1))
    # print('initial dp:', dp)

    for x in range(1, length - 2):
      while queues[x]:
        now = queues[x].popleft()
        nowS, nowN = now
        for i in range(length):
          if not (1 << i) & nowS:
            nextS = nowS | (1 << i)
            nextValue = dp[now] + getValue(A, getAdditionalTriangle(nowS, i))
            print('nextS, nextValue:', bin(nextS), nextValue)
            if nextValue < dp[nextS, nowN + 1]:
              dp[nextS, nowN + 1] = nextValue
              queues[x + 1].append((nextS, nowN + 1))

    # print('dp:', dp)
    return dp[(1 << length) - 1, length - 2]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().minScoreTriangulation(*args), end='\n-----\n')


  test([1, 2, 3])
  test([3, 7, 4, 5])
  test([1, 3, 1, 4, 1, 5])
else:
  print = lambda *args, **kwargs: None
