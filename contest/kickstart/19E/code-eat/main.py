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


def solve(codeGoal, eatGoal):
  if S == 1:
    c, e = slots[0]
    return (1 - codeGoal / c) * e >= eatGoal

  if S == 2:
    c1, e1 = slots[0]
    c2, e2 = slots[1]

    row1 = [c1, c2, codeGoal]
    row2 = [-e1, -e2, eatGoal - (e1 + e2)]
    row3 = [-e1, -e2, eatGoal - (e1 + e2)]

    debug('codeGoal, eatGoal:', codeGoal, eatGoal)
    debug('row1, row2:', row1, row2)

    fac = row2[0] / row1[0]
    for i in range(3):
      row2[i] -= fac * row1[i]  # 消去f1 剩下f2

    fac = row3[1] / row1[1]
    for i in range(3):
      row3[i] -= fac * row1[i]  # 消去f2 剩下f1

    if row2[0] == row2[1] == 0:
      if row2[2] != 0:
        return row2[2] <= 0
      else:
        return True

    res1, res2 = True, True
    f1 = row2[2] / row2[1]
    if row2[1] < 0:  # <=
      res1 = f1 >= 0
    else:
      res1 = f1 <= 1
    debug('row1, row2, f1:', row1, row2, f1)

    f2 = row3[2] / row3[0]
    if row3[0] < 0:  # <=
      res2 = f2 >= 0
    else:  # >=
      res2 = f2 <= 1
    debug('row1, row3, f2:', row1, row3, f2)

    return res1 and res2


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    D, S = list(map(int, input().split()))
    slots = [namedtuple('slot', ['C', 'E'])(*map(int, input().split())) for i in range(S)]
    goals = [namedtuple('day', ['A', 'B'])(*map(int, input().split())) for i in range(D)]

    ans = []
    for goal in goals:
      ans.append('Y' if solve(goal.A, goal.B) else 'N')

    print('Case #{}: {}'.format(caseIndex + 1, ''.join(ans)))
