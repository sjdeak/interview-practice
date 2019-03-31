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

# 可以买入 卖出多次
class Solution:
  def maxProfit(self, prices):  # -> int
    profit = {}
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
          profit[(i, j)] = max(0, prices[j] - prices[i])
    # print('profit', profit)

    dp = {-1:0, 0: 0}
    for j in range(1, len(prices)):
      notSaleI = dp[j-1]
      saleI = max([dp[i-1] + profit[(i, j)] for i in range(0, j)])

      dp[j] = max(notSaleI, saleI)

    # print('dp', dp)

    return dp[len(prices)-1]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxProfit(*args), end='\n-----\n')


  test([7,1,5,3,6,4])
  test([1,2,3,4,5])
  test([7,6,4,3,1])
