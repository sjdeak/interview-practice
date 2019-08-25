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
  # unfinished
  T = int(input())
  for caseIndex in range(T):
    N, K = map(int, input().split())
    dists = list(map(int, input().split()))
    colors = list(map(int, input().split()))

    dogs = defaultdict(list)  # color: [dist1, dist2, ...]
    for i, color in enumerate(colors):
      dogs[color].append(dists[i])
    for i, color in enumerate(colors):
      dogs[color] = sorted(dogs[color])
    # debug('dogs:', dogs)

    ans = min([dp(0, c, -1, 0) for c in colors])
    print('Case #{}: {}'.format(caseIndex + 1, ans))
    dp.cache_clear()
