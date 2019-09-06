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


class Solution:
  def minCostClimbingStairs(self, cost):  # -> int
    length = len(cost)
    dp = {length - 1: cost[-1], length - 2: cost[-2]}

    cost = cost[:-2]
    for i in range(len(cost) - 1, -1, -1):
      dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

    print('dp', dp)

    return min(dp[0], dp[1])


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().minCostClimbingStairs(*args), end='\n-----\n')


  test([10, 15, 20])
  test([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
