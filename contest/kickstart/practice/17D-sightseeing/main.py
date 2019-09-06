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

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, TS, TF = list(map(int, input().split()))  # TF: the latest time you can arrive in city N.
    Cities = [namedtuple('city', ['S', 'F', 'D'])(*(int, input().split())) for i in range(N - 1)]

    print('Case #{}:'.format(caseIndex + 1))
