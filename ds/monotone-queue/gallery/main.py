import os
import sys
from collections import defaultdict, deque
from math import *


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

"""
易知此算法得到的区间必包含所有种类
但如何证明最优性(得到的区间长度最短)?

观察
1. 任何一个最优解 队首必只出现一次  (不然可以把队首去掉，获得更优的解)
=> 所以此算法得到的队首必是最优解的队首

2. 此算法会遍历到所有队首

"""
if __name__ == '__main__':
  N, M = list(map(int, input().split()))
  A = list(map(int, input().split()))
  q = deque()  # usage: Queue
  counter = defaultdict(int)
  ans = (-inf, inf)
  for i, n in enumerate(A):
    q.append(n)
    counter[n] += 1  # 队列里的各种类名画计数器

    # 如果队首表示的名画在队列里出现超过一次，队首出队
    while q and counter[q[0]] >= 2:
      counter[q[0]] -= 1
      q.popleft()

    # print('counter, q:', counter, q)
    if len(list(filter(bool, [value >= 1 for value in counter.values()]))) == M:
      choice = (i - (len(q) - 1), i)
      # print('choice:', choice)
      ans = min(ans, choice, key=lambda t: t[1] - t[0] + 1)
      if q:
        counter[q[0]] -= 1
        q.popleft()

  print(*map(lambda n: n + 1, ans))
