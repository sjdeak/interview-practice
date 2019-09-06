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
  # sys.stdin = open(os.path.expanduser('./in.txt'))
  sys.stdin = open(os.path.expanduser('./A-small-practice.in'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func

"""
dp[i,?, ?] <- dp[i-n, j, j+n-1] + 1  会有多种选法
           dp[i-1,?, ?] + 1
dp[i,j,k] <- dp[
操作只有两种
1. append char
2. 复制黏贴
"""


@dump_args
@lru_cache(None)
def solve(i, j, k):
  if i == 0:
    return 1

  debug('i, j, k:', i, j, k)

  choices = [solve(i - 1, j, k)]  # 操作1 append char
  choices += [solve(i, a, b) for a in range(i + 1) for b in range(a, i + 1)]  # 操作2 复制

  # 操作3 整段黏贴
  if j != -1 and k != -1:  # 剪贴板为空时，上一次操作不可能是黏贴
    clipboardLen = k - j + 1
    if S[j:k + 1] == S[i - clipboardLen + 1:i + 1]:
      choices.append(solve(i - clipboardLen, j, k))

  return min(choices)


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    S = input()
    debug('S:', S)
    # 枚举所有可能的剪贴板内容
    choices = [solve(len(S) - 1, i, j) for i in range(len(S)) for j in range(i, len(S))]
    choices.append(solve(len(S) - 1, '?', '?'))
    ans = min(choices)

    print('Case #{}: {}'.format(caseIndex + 1, ans if ans != inf else 'IMPOSSIBLE'))
