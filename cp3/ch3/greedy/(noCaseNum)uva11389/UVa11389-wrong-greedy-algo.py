import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter
from operator import itemgetter
from math import sqrt


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')

if __name__ == '__main__':
  for caseIndex in count(1):
    N, D, R = list(map(int, input().split()))
    if not N: break
    mornings = list(map(int, input().split()))
    nights = list(map(int, input().split()))

    choices = sorted([(i, j, 0 if m + n - D <= 0 else m + n - D, m + n - D)
                      for i, m in enumerate(mornings)
                      for j, n in enumerate(nights)], key=itemgetter(3))

    ans = 0
    used = set()
    for choice in choices:
      i, j, val, foo = choice
      if i in used or j in used:
        continue
      ans += val

    print(ans * R)
