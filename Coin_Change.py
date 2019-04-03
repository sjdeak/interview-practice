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
  def coinChange(self, coins, amount):  # -> int
    dp = {0: 0}
    for n in range(1, amount + 1):
      choices = [dp[n - c] + 1 for c in coins if n - c >= 0 and dp[n - c] != -1]
      if choices:
        dp[n] = min(choices)
      else:
        dp[n] = -1

    print('dp', dp)
    return dp[amount]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().coinChange(*args), end='\n-----\n')


  test([1, 2, 5], 11)
  test([2], 3)

else:
  print = lambda *args, **kwargs: None
