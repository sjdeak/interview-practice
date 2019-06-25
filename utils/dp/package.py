import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1000000)


# 无限背包统计方案数
def PackageInfinite(nums, targetSum):
  dp = defaultdict(int)
  length = len(nums)
  for i in range(length):
    for s in range(1, targetSum + 1):
      if not i:
        dp[(0, nums[0])] = 1
        continue

      methodsCnt = 0
      for k in range(s // nums[i]):
        methodsCnt += dp[i - 1, s - k * nums[i]]

  print('dp', dp)
  return dp[length - 1, targetSum]
