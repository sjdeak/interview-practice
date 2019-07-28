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
    K, N = list(map(int, input().split()))
    Spots = list(map(int, input().split()))
    Costs = list(map(int, input().split()))

    ans = inf

    for j in range(N):  # 枚举仓库地点
      res = Costs[j]
      tmpCosts = Costs.copy()
      for i, tmpCost in enumerate(tmpCosts):
        tmpCosts[i] += abs(Spots[j] - Spots[i])
      # debug('base, tmpCosts:', res, tmpCosts)
      tmpCosts = tmpCosts[:j] + tmpCosts[j + 1:]
      res += sum(sorted(tmpCosts)[:K])

      # debug('res:', res)

      ans = min(ans, res)

    print('Case #{}: {}'.format(caseIndex + 1, ans))
