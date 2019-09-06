import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter
from operator import itemgetter
from math import sqrt


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./icpc-data/in.txt'))
  # sys.stdout = open(os.path.expanduser('~/data/out.txt'), 'w')

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    X = input()
    Z = input()

    dp = {}

    for i in range(0, len(X)):
      for j in range(0, len(Z)):
        # print('(i, j):', (i, j))
        if not i:
          if i == j == 0:
            dp[(i, j)] = int(X[0] == Z[0])
          else:
            dp[(i, j)] = 0
          continue
        if not j:
          c = Counter(X[:i + 1])
          dp[(i, j)] = c[Z[j]]
          continue

        dp[(i, j)] = dp[(i - 1, j)] + (dp[i - 1, j - 1] if X[i] == Z[j] else 0)

    # print('dp', dp)
    print(dp[(len(X) - 1, len(Z) - 1)])
