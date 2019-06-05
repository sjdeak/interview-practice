# https://leetcode.com/problems/two-city-scheduling/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


class Solution:
  def twoCitySchedCost(self, costs):  # -> int
    N = len(costs)
    costA = {i: c[0] for i, c in enumerate(costs)}
    costB = {i: c[1] for i, c in enumerate(costs)}
    costs = [(i, *c) for i, c in enumerate(costs)]  # (i, 去A地的费用, 去B地的费用)
    seqA = sorted(costs, key=itemgetter(1))
    seqB = sorted(costs, key=itemgetter(2))

    print('seqA:', seqA)
    print('seqB:', seqB)

    ans = 0
    used = set()
    pa, pb = 0, 0
    while True:
      print('used:', used)

      try:
        while seqA[pa][0] in used: pa += 1
        while seqB[pb][0] in used: pb += 1
      except IndexError:
        break

      paId, pbId = seqA[pa][0], seqB[pb][0]
      if paId == pbId:
        nowId = paId
        nowPa, nowPb = pa, pb
        pa, pb = pa + 1, pb + 1

        try:
          while seqA[pa][0] in used: pa += 1
          while seqB[pb][0] in used: pb += 1
        except IndexError:
          pass

        choices = []
        if pa < 2 * N:  # A用新pa指向的Id  B用nowId
          cost = costA[seqA[pa][0]] + costB[nowId]
          choices.append((cost, pa, nowPb, seqA[pa][0], nowId))
        if pb < 2 * N:  # A用nowId  B用新pb指向的Id
          cost = costA[nowId] + costB[seqB[pb][0]]
          choices.append((cost, nowPa, pb, nowId, seqB[pb][0]))

        choice = min(choices, key=itemgetter(0))
        paId, pbId = choice[3:]
        pa, pb = choice[1:3]

      ans += costA[paId] + costB[pbId]
      print('ans:', ans)
      used.update([paId, pbId])

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().twoCitySchedCost(*args), end='\n-----\n')


  test([[10, 20], [30, 200], [400, 50], [30, 20]])
  test([[10, 10], [30, 200], [400, 50], [30, 20]])
  test([[10, 10], [20, 20], [400, 50], [30, 20]])
  test([[70, 311], [74, 927], [732, 711], [126, 583], [857, 118], [97, 928], [975, 843], [175, 221], [284, 929],
        [816, 602], [689, 863], [721, 888]])
  test([[70, 311], [74, 927], [732, 711], [126, 583], [857, 118], [97, 928], [175, 221], [284, 929], [816, 602],
        [689, 863]])
  test([[70, 311], [74, 927], [126, 583], [857, 118], [97, 928], [175, 221], [284, 929], [816, 602]])
else:
  print = lambda *args, **kwargs: None
