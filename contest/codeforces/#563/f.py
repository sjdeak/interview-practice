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


def sendInteractiveCommand(cmd):
  print(cmd)
  sys.stdout.flush()
  return input()


def findHidden(now):
  cmdRes = sendInteractiveCommand(f'd {now}')
  if cmdRes.startswith('Wrong answer'):
    return now

  if len(graph[now]) == 1:
    return findHidden(graph[now][0])
  else:
    childA, childB = graph[now]
    childADis, childBDis = int(sendInteractiveCommand(f'd {childA}')), int(sendInteractiveCommand(f'd {childB}'))
    if childADis < childBDis:
      return findHidden(childA)
    else:
      return findHidden(childB)


if __name__ == '__main__':
  N = int(input())
  graph = defaultdict(list)
  for i in range(N - 1):
    u, v = list(map(int, input().split()))
    graph[u].append(v)

  ans = findHidden(1)
  print('! {}'.format(ans))
