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

if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


# on grid
def manhattanDistance(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return abs(x2 - x1) + abs(y2 - y1)


T = int(input())


def tsp(cities, dist):
  length = len(cities)
  statesVisited = set()

  @lru_cache(None)
  def dp(vis, now):
    if vis == (1 << length) - 1 and now == 0:
      return 0

    statesVisited.add((vis, now))
    debug('statesVisited:', statesVisited)

    choices = []
    for i in range(length):
      if i == now: continue
      nextState = (vis | (1 << i), i)
      if nextState not in statesVisited:
        choices.append(dp(*nextState) + dist[now, i])
        debug('choices:', choices)

    return min(choices or [inf])

  return dp(0, 0)


for caseIndex in range(T):
  R, C = map(int, input().split())
  x, y = map(int, input().split())

  points = [(x, y)] + [tuple(map(int, input().split())) for i in range(int(input()))]
  debug('points:', points)

  length = len(points)

  dist = {(i, j): manhattanDistance(points[i], points[j]) for i in range(length) for j in range(i + 1, length)}
  dist.update({(j, i): manhattanDistance(points[i], points[j]) for i in range(length) for j in range(i + 1, length)})

  print('The shortest path has length {}'.format(tsp(points, dist)))
