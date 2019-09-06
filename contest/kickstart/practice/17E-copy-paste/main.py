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
  # sys.stdin = open(os.path.expanduser('./in-sample.txt'))
  # sys.stdin = open(os.path.expanduser('./in.txt'))
  sys.stdin = open(os.path.expanduser('./A-large-practice.in'))
  # sys.stdin = open(os.path.expanduser('./A-small-practice.in'))
  sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func

"""
操作只有两种
1. append char
2. 复制黏贴
"""


@lru_cache(None)
def solve(i, j, k):
  if i == 0:
    if j == '_' and k == '_':
      return 1
    return 2 if j == k == 0 else 1
  # debug('i, j, k:', i, j, k)

  choices = []
  # 操作1 append char
  if j != '_' and k != '_':
    for a in range(i):  # 0~i-1
      for b in range(a, i):
        if S[a:b + 1] == S[j:k + 1]:
          choices.append(solve(i - 1, a, b) + 1)  # 只是append
        else:
          choices.append(solve(i - 1, a, b) + 2)  # append, 然后再复制
    choices.append(solve(i - 1, '_', '_') + 2)  # 原来剪贴板是空的  append, 然后再复制
  else:
    choices.append(solve(i - 1, '_', '_') + 1)

  # 操作2 复制黏贴
  if j != '_' and k != '_':
    for cbLen in range(1, (i + 1) // 2 + 1):  # 剪贴板的长度必 <= len // 2
      for a in range(i + 1):
        b = a + cbLen - 1
        if b <= i - cbLen and S[a:b + 1] == S[i - cbLen + 1:i + 1]:
          if S[a:b + 1] == S[j:k + 1]:
            choices.append(solve(i - cbLen, a, b) + 1)  # 只是一步黏贴
          else:
            choices.append(solve(i - cbLen, a, b) + 2)  # 黏贴a,b 再复制成j,k

  # debug('choices:', choices)
  return min(choices)


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    S = input()
    # debug('S:', S)
    # 枚举所有可能的剪贴板内容
    choices = [solve(len(S) - 1, i, j) for i in range(len(S)) for j in range(i, len(S))]
    choices.append(solve(len(S) - 1, '_', '_'))
    # choices = [solve(3, 0, 1)]
    # choices = [solve(1, 0, 1)]
    ans = min(choices)
    print('Case #{}: {}'.format(caseIndex + 1, ans))

    solve.cache_clear()
