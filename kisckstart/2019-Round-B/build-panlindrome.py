import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter
from operator import itemgetter
from math import sqrt


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open('../../icpc-data/in.txt')
  # sys.stdout = open(os.path.expanduser('~/data/out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


def solve():
  global S, N, Q
  dp = {}
  length = len(S)

  for i in range(length - 1, -1, -1):
    for j in range(i, length):
      debug('i, j: ', i, j)
      if i == j:
        dp[(i, j)] = (True, {S[i]})
        continue
      if j - i + 1 == 2:
        dp[(i, j)] = (True, set()) if S[i] == S[j] else (False, {S[i], S[j]})

      if (i - j + 1) % 2:
        oddChar = dp[(i + 1, j)][1]
        if dp[(i + 1, j)][0]:
          dp[(i, j)] = (True, {S[i]})
          continue
        elif len(oddChar) == 2 and S[i] in oddChar:
          s = {*oddChar}
          s.remove(S[i])
          dp[(i, j)] = (True, s)
          continue

        oddChar = dp[(i, j - 1)][1]
        if dp[(i, j - 1)][0]:
          dp[(i, j)] = (True, {S[j]})
          continue
        elif len(oddChar) == 2 and S[j] in oddChar:
          s = {*oddChar}
          s.remove(S[j])
          dp[(i, j)] = (True, s)
          continue

        dp[(i, j)] = (False, {*oddChar, S[j]})

      else:  # 子串长度为偶数
        oddChar = dp[(i + 1, j)][1]
        if dp[(i + 1, j)][0]:
          if len(oddChar) == 1 and S[i] in oddChar:
            dp[(i, j)] = [True, set()]
            continue

        oddChar = dp[(i, j - 1)][1]
        if dp[(i, j - 1)][0]:
          if len(oddChar) == 1 and S[j] in oddChar:
            dp[(i, j)] = [True, set()]
            continue

        dp[(i, j)] = [False, {*oddChar, S[j]}]

  debug('dp:', dp)
  return dp


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, Q = map(int, input().split())
    S = input()
    dp = solve()
    debug('dp', dp)
    ans = 0
    for _ in range(Q):
      l, r = map(int, input().split())
      if dp[(l - 1, r - 1)][0]:
        ans += 1

    print("Case #{}: {}".format(caseIndex + 1, ans))
