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


def cmp(a, b):
  ta, fa, _ = a
  tb, fb, _ = b

  if ta * fb < tb * fa:
    return -1  # a negative number for less-than
  elif ta * fb > tb * fa:
    return 1  # a positive number for greater-than
  else:
    return 0  # zero for equality


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(1, T + 1):
    input()

    # [(要花几天, 每超时一天的罚款, 序号)]
    jobs = [list(map(int, input().split())) + [i + 1] for i in range(int(input()))]
    jobs.sort(key=cmp_to_key(cmp))

    print(*map(itemgetter(2), jobs))
    if caseIndex != T:
      print()
