# uva507-jill-rides-again
import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter, defaultdict
from operator import itemgetter
from math import inf


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./data/in.txt'))
  # sys.stdout = open(os.path.expanduser('./data/out.txt'), 'w')


def max1dRangeSum(A):
  length = len(A)
  dp = {}
  dp[0] = (A[0], 0)
  for i in range(1, length):
    preSum, preSt = dp[i - 1]
    if preSum < 0:
      dp[i] = (A[i], i)
    else:
      dp[i] = (preSum + A[i], preSt)

  # print('dp:', dp)

  # * 推导结果 *#
  ans = -inf
  ansSt, ansEd = 0, 0
  for i in range(length):
    sum, st = dp[i]
    if sum > ans or (sum == ans and i - st > ansEd - ansSt):  # 当有若干区间的区间和都是最大时，返回最长的区间
      ans = sum
      ansSt, ansEd = st, i

  # print('ans, ansSt, ansEd:', ans, ansSt, ansEd)
  return ans, ansSt, ansEd


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N = int(input())
    A = [int(input()) for i in range(N - 1)]

    ans, l, r = max1dRangeSum(A)
    if ans > 0:
      print('The nicest part of route {} is between stops {} and {}'.format(caseIndex + 1, l + 1, r + 2))
    else:
      print('Route {} has no nice parts'.format(caseIndex + 1))
