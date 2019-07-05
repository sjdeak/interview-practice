import os
import sys
from collections import deque
from math import *


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in2.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

if __name__ == '__main__':
  N, M = list(map(int, input().split()))
  A = list(map(int, input().split()))
  q = deque()  # usage demo: Queue
  qSum = 0
  ans = -inf
  for i, n in enumerate(A):
    if len(q) < M:
      q.append(n)
      qSum += n
      ans = max(ans, qSum)
    else:
      while q and q[0] < 0:
        qSum -= q[0]
        q.popleft()

      if len(q) == M:
        qSum -= q[0]
        q.popleft()
        q.append(n)
        qSum += n
        ans = max(ans, qSum)

  print(ans)
