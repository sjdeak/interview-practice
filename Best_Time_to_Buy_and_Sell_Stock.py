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
  def maxProfit(self, prices):  # -> int
    length = len(prices)
    if length < 2:
      return 0
    dp = {1: prices[1] - prices[0]}

    minValue = min(prices[:2])
    for i in range(2, length):
      dp[i] = max(dp[i - 1], prices[i] - minValue)
      minValue = min(minValue, prices[i])

    return max(0, dp[length - 1])


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxProfit(*args), end='\n-----\n')


  test([7, 1, 5, 3, 6, 4])
  test([7, 6, 4, 3, 1])
