import os
import sys
from collections import deque
from math import *


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in-large.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


def getPrefixSum(A):
  res = [A[0]]
  for i in range(1, len(A)):
    res.append(A[i] + res[i - 1])
  return res


# 正统单调队列做法
# 遍历出每个以i结尾的子序列的和
if __name__ == '__main__':
  N, M = list(map(int, input().split()))
  A = list(map(int, input().split()))
  ps = getPrefixSum(A)
  q = deque()  # 队列里存放所有可能与i组合成解的k
  ans = -inf

  for i in range(len(A)):
    while q and q[0] < i - M:  # 保证组合出来的子序列长度不超过M
      q.popleft()
    if q:
      ans = max(ans, ps[i] - ps[q[0]])
    while q and ps[q[-1]] >= ps[i]:  # 保持队列单增
      q.pop()

    q.append(i)

  print(ans)
