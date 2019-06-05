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
  # sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


def sieve(n):
  """返回[0, n]内的素数组成的迭代器"""
  isp = [1] * (n + 1)
  isp[0] = isp[1] = 0
  pCnt = 0
  for i in range(2, n + 1):
    if isp[i]:
      pCnt += 1
      for j in range(i * i, i * (n // i + 1), i):
        isp[j] = pCnt


if __name__ == '__main__':
  N = int(input())
  ans = []
  primeCnt = 0

  isp = [(True, 0)] * (N + 1)
  isp[0] = isp[1] = (False, 0)
  pCnt = 0
  for i in range(2, N + 1):
    if isp[i][0]:
      pCnt += 1
      isp[i] = (True, pCnt)
      for j in range(i * i, i * (N // i + 1), i):
        isp[j] = (False, pCnt)
      # print('isp:', isp)

  print(*map(itemgetter(1), isp[2:]))
