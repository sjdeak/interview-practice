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
  # sys.stdin = open(os.path.expanduser('./A-small-practice.in'))
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


# todo 这题要总结一下为什么main-wrong是不对的
# @dump_args
@lru_cache(None)
def solve(i, j, k):
  if i < 0:
    return 0
  if i == 0:
    return 1

  # debug('i, j, k:', i, j, k)

  choices = [solve(i - 1, j, k) + 1]
  for clipboardLen in range(1, i // 2 + 1):  # 剪贴板的长度必 <= i // 2
    for a in range(i + 1):
      b = a + clipboardLen - 1

      if S[a:b + 1] == S[i - clipboardLen + 1:i + 1]:
        if j == '?' and k == '?':
          choices.append(solve(i - clipboardLen, a, b) + 2)
          # choices.append(solve(i - clipboardLen, '?', '?') + 2)
        else:
          if a == j and b == k:
            choices.append(solve(i - clipboardLen, a, b) + 1)  # 只是一步黏贴
          else:
            choices.append(solve(i - clipboardLen, a, b) + 2)  # 黏贴a,b 再复制成j,k
  # debug('choices:', choices)
  return min(choices)


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    S = input()
    debug('S:', S)
    # 枚举所有可能的剪贴板内容

    ans = solve(len(S) - 1, '?', '?')

    print('Case #{}: {}'.format(caseIndex + 1, ans if ans != inf else 'IMPOSSIBLE'))
