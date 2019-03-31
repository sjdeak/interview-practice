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

d = float(input())
N = int(input())
users = [tuple(map(float, input().split())) for i in range(N)]
length = len(users)


def dist(i, j):
  deltaX = users[i][0] - users[j][0]
  deltaY = users[i][1] - users[j][1]
  return sqrt(deltaX ** 2 + deltaY ** 2)


edges = {}
for i, user in enumerate(users):
  for j in range(i + 1, length):
    edges[(i, j)] = dist(i, j) <= d
    edges[(j, i)] = edges[(i, j)]

# print('edges', edges)

sets = []

def dfs(now):
  group = None
  if not any([now in s for s in sets]):
    group = {now}
    sets.append(group)
  else:
    for s in sets:
      if now in s:
        group = s

  for j in range(N):
    if now == j:
      continue
    if edges[(now, j)] and not j in group:
      group.add(j)
      dfs(j)


for i in range(N):
  dfs(i)

print(list(map(list, sets)))

"""
自制测试数据

1
2
1 1
2 1


"""
