# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aae
import os
import sys
from math import *


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in2.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


class Stack:
  def __init__(self):
    self.data = []

  def push(self, x):  # -> None
    self.data.append(x)

  def pop(self):  # -> item
    return self.data.pop()

  def top(self):  # -> item on top
    return self.data[-1] if len(self.data) else None

  def __len__(self):
    return len(self.data)

  def __bool__(self):
    return bool(self.data)


def largestRectangleArea(heights):  # -> int
  s = Stack()
  heights += [0]
  ans = 0
  for h in heights:
    if not s or h > s.top()[1]:
      s.push((1, h))  # 入栈一个矩形 (width, height)
    else:
      cnt = 0
      # 计算单增序列里的矩形最大值，即计算所有以s.top()为末尾的矩形大小
      while s and s.top()[1] > h:
        recPopped = s.pop()
        cnt += recPopped[0]
        ans = max(ans, cnt * recPopped[1])
      s.push((cnt + 1, h))

  return ans


# O(n^3)
def getCountAbove():
  res = {}
  for i, row in enumerate(Grid):
    for j, n in enumerate(row):
      minimum, maximum = inf, -inf
      cnt = 0

      for k in range(i, -1, -1):
        maximum = max(maximum, Grid[k][j])
        minimum = min(minimum, Grid[k][j])
        if maximum - minimum <= K:
          cnt += 1
      res[i, j] = cnt
  return res


def transportMatrix(mat):
  if not mat:
    return mat
  R, C = len(mat), len(mat[0])
  return [[mat[r][c] for r in range(R)] for c in range(C)]


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    R, C, K = map(int, input().split())
    Grid = transportMatrix([list(map(int, input().split())) for r in range(R)])
    # debug('Grid:', Grid)

    # 从(i,j)开始往上有多少个连续的格子，使得最薄的格子和最厚的格子间的厚度差不超过K
    cntAbove = getCountAbove()
    # print('cntAbove:', *cntAbove.items(), sep='\n')

    ans = 0
    for i in range(C):
      heights = [cntAbove[i, j] for j in range(R)]
      ans = max(ans, largestRectangleArea(heights))

    print('Case #{}: {}'.format(caseIndex + 1, ans))
