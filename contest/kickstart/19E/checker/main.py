import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy

sys.setrecursionlimit(1000000)


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


@dump_args
@lru_cache(None)
def dpOdd(n):
  # debug('dpOdd, n:', n)
  if n == 1:
    return 1

  res = 0
  for i in range(2, n + 1):
    if n % i == 0 and i % 2:  # n是偶数 i是奇数
      res += dpOdd(n // i) + 1
      break
  for i in range(2, n + 1):
    if n % i == 0 and i % 2 == 0:  # i是偶数
      res += dpOdd(n // i) + 1
      break

  return 1


@dump_args
@lru_cache(None)
def dpEven(n):
  # debug('dpEven, n:', n)
  if n == 1:
    return 0

  for i in range(2, n + 1):
    if n % i == 0 and i % 2 == 0:
      return dpEven(n // i) + 1

  return 0


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    L, R = list(map(int, input().split()))

    ans = 0
    for i in range(L, R + 1):
      debug('i:', i)
      if abs(dpOdd(i) - dpEven(i)) <= 2:
        ans += 1
    print('Case #{}: {}'.format(caseIndex + 1, ans))
