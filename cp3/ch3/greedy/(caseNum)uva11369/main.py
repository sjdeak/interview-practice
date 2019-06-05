"""
AD exchange arguments 例题变体 (轻微变化)

所有任务只要没有开始做，每天都要付罚款
"""
import os, sys
from functools import cmp_to_key
from itertools import count, combinations
from collections import namedtuple, Counter
from operator import itemgetter
from math import sqrt


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(1, T + 1):
    [N] = list(map(int, input().split()))
    prices = sorted(list(map(int, input().split())), reverse=True)

    ans = sum(prices[i] for i in range(2, len(prices), 3))
    print(ans)
