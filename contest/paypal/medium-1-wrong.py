import os, sys, shutil, glob, re
import time, calendar
from bisect import bisect_left
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from queue import Queue

# 题面看错 理解成找不相交区间了
N = int(input())
intervals = [tuple(map(int, input().split())) for i in range(N)]
intervals.sort(key=itemgetter(1))

before = {}
for i, interval in enumerate(intervals):
  st, ed = interval
  before[i] = bisect_left(map(itemgetter(1), interval), st)
print('before', before)

dp = {0: 1}
for j in range(1, len(intervals)):
  useJ = j - before[j] + 1
  notUseJ = dp[j - 1]
  dp[j] = max(useJ, notUseJ)

"""
solution = []
def findSolution(j):
  if not j:
    return
  if dp[j] == dp[j-1]:
    findSolution(j-1)
  if dp[j] == dp[before[j]]+1:
    solution.append(j)
    findSolution(before[j])
"""
