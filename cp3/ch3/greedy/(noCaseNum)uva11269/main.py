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
    [N] = list(map(int, input().split()))
    tas = sorted(list(map(int, input().split())))
    tbs = sorted(list(map(int, input().split())))

    ans = 0
    used = set()
    for i in range(N):
      ans += 0 if mornings[i] + nights[i] - D < 0 else mornings[i] + nights[i] - D

    print(ans * R)
