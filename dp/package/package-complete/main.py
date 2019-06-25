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


# O( len(nums) * volume )
def completePackage(items, volume):
  dp = defaultdict(int)
  length = len(items)
  ans = -inf
  # dp[i,vol] 从前i种物品里选，装容量为vol的背包，可得到的最大价值
  for i in range(length):
    for s in range(1, volume + 1):  # s: size
      if items[i].vol <= s:
        # 细粒度转移  方便但也不够直观
        dp[(i, s)] = max(dp[i - 1, s], dp[i, s - items[i].vol] + items[i].val)
      else:
        dp[(i, s)] = dp[i - 1, s]
      ans = max(ans, dp[(i, s)])

  # debug('dp', dp)
  return ans


if __name__ == '__main__':
  N, Volume = list(map(int, input().split()))
  items = [namedtuple('item', ['vol', 'val'])(*map(int, input().split())) for i in range(N)]

  print(completePackage(items, Volume))
