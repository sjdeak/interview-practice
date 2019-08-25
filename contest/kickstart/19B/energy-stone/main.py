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


def cmp(a, b):
  left = a.S * b.L
  right = b.S * a.L

  if left < right:
    return -1  # a negative number for less-than
  elif left > right:
    return 1  # a positive number for greater-than
  else:
    return 0  # zero for equality


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N = int(input())
    # S: 吃掉要花多少时间 E: 吃掉可获得多少能量 L: 每秒流失多少能量
    A = [namedtuple('stone', ['S', 'E', 'L'])(*map(int, input().split())) for i in range(N)]

    A.sort(key=cmp_to_key(cmp))
    maxTime = sum(map(itemgetter(0), A))

    debug('A, maxTime:', A, maxTime)

    dp = defaultdict(int)
    length = len(A)
    ans = -inf

    # dp[i][t] 总共用t秒, 从前i个石头里选, 可以得到的最大收益
    # 这里的t并不是容量限制  而是必须要维护的辅助变量 不然无法获知损耗量是多少
    for i in range(length):
      for t in range(maxTime + 1):
        if i == 0:
          dp[i, t] = A[0].E if A[0].S <= t else 0
          ans = max(ans, dp[i, t])
          continue

        if A[i].S <= t:
          dp[i, t] = max(dp[i - 1, t], dp[i - 1, t - A[i].S] + A[i].E - A[i].L * (t - A[i].S))
        else:
          dp[i, t] = dp[i - 1, t]
        ans = max(ans, dp[i, t])

    debug('dp:', dp)

    print('Case #{}: {}'.format(caseIndex + 1, ans))
