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


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

# WENS
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def walk(now, c, vis):
  vis.add(now)
  x, y = now
  i = list('WENS').index(c)
  newX, newY = x + dx[i], y + dy[i]
  if (newX, newY) in vis:
    return walk((newX, newY), c, vis)
  else:
    return newX, newY


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, R, C, *st = map(int, input().split())
    st = tuple(st[::-1])  # c, r   即x,y
    commands = input()

    vis = set()
    now = st
    for c in commands:
      now = walk(now, c, vis)
      # debug('c, now:', c, now)

    print('Case #{}: {} {}'.format(caseIndex + 1, now[1], now[0]))
