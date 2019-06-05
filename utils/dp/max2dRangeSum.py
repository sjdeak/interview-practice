# uva108-maximum-sum
import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter, defaultdict
from operator import itemgetter
from math import inf


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./data/in.txt'))
  # sys.stdout = open(os.path.expanduser('./data/out.txt'), 'w')


def max2dRangeSum(A):
  length = len(A)
  dp = defaultdict(int)
  for i in range(length):
    for j in range(length):
      dp[i, j] = A[i][j]
      if j > 0:
        dp[i, j] += dp[i, j - 1]
      if i > 0:
        dp[i, j] += dp[i - 1, j]
      if i > 0 and j > 0:
        dp[i, j] -= dp[i - 1, j - 1]
  # print('dp:', dp)

  ans = -inf
  for i in range(length):
    for j in range(length):
      for k in range(i, length):
        for l in range(j, length):
          curArea = dp[k, l] - dp[i - 1, l] - dp[k, j - 1] + dp[i - 1, j - 1]

          # print('i,j,k,l, curArea:', i, j, k, l, curArea)

          ans = max(ans, curArea)

  return ans


if __name__ == '__main__':
  N = int(input())
  nums = []
  for line in sys.stdin:
    nums += list(map(int, line.split()))
  A = [nums[i:i + N] for i in range(0, N ** 2, N)]

  print(max2dRangeSum(A))
