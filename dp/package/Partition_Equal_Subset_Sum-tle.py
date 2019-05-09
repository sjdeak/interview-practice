import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue


def refreshGlobals():
  pass


refreshGlobals()


# TLE: O( len(nums) * targetSum )
def subsetSum(nums, targetSum):
  dp = defaultdict(bool)
  length = len(nums)
  for i in range(0, length):
    for s in range(1, targetSum + 1):
      if not i:
        dp[(i, nums[i])] = True
      else:
        dp[(i, s)] = dp[i - 1, s] or dp[i - 1, s - nums[i]]

  print('dp', dp)
  return dp[length - 1, targetSum]


# TLE: O( 2^len(nums) ) todo 为什么反而更慢了?
def subsetSumAdvancedDP(nums, targetSum):
  dp = defaultdict(bool)
  length = len(nums)

  queues = [deque() for _ in range(length + 1)]
  queues[0].append((0, nums[0]))
  dp[0, nums[0]] = True

  for x in range(0, length - 1):
    while queues[x]:
      now = queues[x].popleft()
      i, s = now  # dp[i,s] = True
      dp[i + 1, s + nums[i + 1]] = True
      dp[i + 1, s] = True

      if s + nums[i + 1] <= targetSum:
        queues[x + 1].append((i + 1, s + nums[i + 1]))
      queues[x + 1].append((i + 1, s))

  print('dp', dp)
  return dp[length - 1, targetSum]



class Solution:
  def canPartition(self, nums):  # -> bool
    if sum(nums) % 2:
      return False
    else:
      return subsetSumAdvancedDP(nums, sum(nums) // 2)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().canPartition(*args), end='\n-----\n')


  test([1, 5, 11, 5])
  test([1, 2, 3, 5])
  test(
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100])

  # print('subsetSum([1,5,11,5], 11): ', subsetSum([1, 5, 11, 5], 11))
else:
  print = lambda *args, **kwargs: None
