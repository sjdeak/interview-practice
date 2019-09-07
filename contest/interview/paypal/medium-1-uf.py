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

N = int(input())
intervals = [tuple(map(int, input().split())) for i in range(N)]
intervals.sort(key=itemgetter(1))

before = {}
for i, interval in enumerate(intervals):
  st, ed = interval
  before[i] = bisect_left(list(map(itemgetter(1), intervals)), st)
print('before', before)


def getLeft(bf, j):
  if bf == j:
    return intervals[bf][0]
  else:
    return min(map(itemgetter(0), intervals[bf:j + 1]))


ansVal = 0
ans = []
for j in range(0, len(intervals)):
  nowSt, nowEd = intervals[j]

  bf = before[j]
  cnt = j - bf + 1  # 含j弹幕时的热度(相交弹幕总数)

  if cnt > ansVal:
    ansVal = cnt
    left = getLeft(bf, j)
    ans = [(left, nowEd)]
  elif cnt == ansVal:
    left = getLeft(bf, j)
    ans.append((left, nowEd))

  print('j, cnt', j, cnt)

print('ans', ans)

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
