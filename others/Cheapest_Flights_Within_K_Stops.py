# https://leetcode.com/problems/cheapest-flights-within-k-stops/
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
  def findCheapestPrice(self, n, flights, src, dst, K):  # -> int
    dp = {(src, 0): 0}
    for u, v, cost in flights:
      if u == src:
        dp[v, 0] = cost

    print('initial dp:', dp)

    for k in range(K + 1):
      for i in range(n):
        if k == 0:
          if (i, 0) not in dp:
            dp[i, 0] = -1
          continue

        print('i, k:', i, k)

        choices = []
        if dp[i, k - 1] != -1:
          choices.append(dp[i, k - 1])

        for u, v, cost in flights:  # u -> v
          # print('u,v,cost:', u, v, cost)
          if v == i and dp[u, k - 1] != -1:  # i=2 k=1
            choices.append(dp[u, k - 1] + cost)

        print('choices:', choices)
        dp[i, k] = min(choices or [-1])

    print('dp', dp)
    return min([dp[dst, k] for k in range(K + 1) if dp[dst, k] != -1] or [-1])


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findCheapestPrice(*args), end='\n-----\n')


  test(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
  test(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)
  test(5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1)

else:
  print = lambda *args, **kwargs: None
