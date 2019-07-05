import os
import sys


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
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


def getFAbove():
  dp = {}
  for i, row in enumerate(Grid):
    for j, ch in enumerate(row):
      if i == 0:
        dp[i, j] = int(ch == 'F')
      else:
        dp[i, j] = dp[i - 1, j] + 1 if ch == 'F' else 0

  return dp


if __name__ == '__main__':
  N, M = list(map(int, input().split()))
  Grid = [input().split() for i in range(N)]

  # 从(i,j)开始往上有多少个连续的F
  fAbove = getFAbove()
  # print('fAbove:', *fAbove.items(), sep='\n')

  ans = 0
  for i in range(N):
    heights = [fAbove[i, j] for j in range(M)]
    ans = max(ans, largestRectangleArea(heights))

  print(3 * ans)
