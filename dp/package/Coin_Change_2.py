# https://leetcode.com/problems/coin-change-2/
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


def refreshGlobals():
  pass


refreshGlobals()


def packageInfinite(nums, targetSum):
  dp = defaultdict(int)
  length = len(nums)
  dp.update({(i, 0): 1 for i in range(length)})
  for k in range(targetSum // nums[0] + 1):
    dp[(0, k * nums[0])] = 1

  for i in range(1, length):
    for s in range(1, targetSum + 1):

      methodsCnt = 0
      for k in range(s // nums[i] + 1):
        methodsCnt += dp[i - 1, s - k * nums[i]]
      dp[i, s] = methodsCnt

  print('dp', dp)
  return dp[length - 1, targetSum]


class Solution:
  def change(self, amount, coins):  # -> int
    return packageInfinite(coins, amount)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().change(*args), end='\n-----\n')


  test(5, [1, 2, 5])
  test(3, [2])
  test(10, [10])
else:
  print = lambda *args, **kwargs: None
