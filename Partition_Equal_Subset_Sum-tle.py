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


class Solution:
  def canPartition(self, nums):  # -> bool
    if sum(nums) % 2:
      return False
    else:
      return subsetSum(nums, sum(nums) // 2)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().canPartition(*args), end='\n-----\n')


  test([1, 5, 11, 5])
  test([1, 2, 3, 5])

  # print('subsetSum([1,5,11,5], 11): ', subsetSum([1, 5, 11, 5], 11))
else:
  print = lambda *args, **kwargs: None
