"""
exchange arguments

任意一种安排方式
可以证明: 如果按照我的贪心方法对其中特定两对做处理  结果一定会更优

也就是说 直接用贪心方法构造出来的解比任意一种安排方式都优
"""
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
    mornings = sorted(list(map(int, input().split())), reverse=True)
    nights = sorted(list(map(int, input().split())))

    ans = 0
    used = set()
    for i in range(N):
      ans += 0 if mornings[i] + nights[i] - D < 0 else mornings[i] + nights[i] - D

    print(ans * R)
