"""
已知: soldiers
条件: 士兵接受完命令就执行
求: 下达命令的顺序，使得所有任务做完的最终时间最早
简化题面:
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


def cmp(a, b):
  b1, j1 = a
  b2, j2 = b
  left = max(b1 + j1, b1 + b2 + j2)
  right = max(b2 + j1, b1 + b2 + j1)

  if left < right:
    return -1  # a negative number for less-than
  elif left > right:
    return 1  # a positive number for greater-than
  else:
    return 0  # zero for equality


if __name__ == '__main__':
  for caseIndex in count(1):
    [N] = list(map(int, input().split()))
    if not N: break
    soldiers = [namedtuple('soldier', ['B', 'J'])(*map(int, input().split()))
                for i in range(N)]
    soldiers.sort(key=cmp_to_key(cmp))

    ans, now = 0, 0
    for i, s in enumerate(soldiers):
      now += s.B
      ans = max(ans, now + s.J)

    print('Case {}: {}'.format(caseIndex, ans))
