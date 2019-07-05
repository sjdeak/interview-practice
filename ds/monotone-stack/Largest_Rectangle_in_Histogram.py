# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
import os
import sys

sys.setrecursionlimit(1000000)


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


class Solution:
  def largestRectangleArea(self, heights):  # -> int
    s = Stack()
    heights += [0]
    ans = 0
    for h in heights:
      if not s or h > s.top()[1]:
        s.push((1, h))  # 入栈一个矩形 (width, height)
      else:
        cnt = 0
        # 计算单增序列里的矩形最大值，即计算所有以s.top()为末尾的矩形大小
        while s.top() is not None and s.top()[1] > h:
          recPopped = s.pop()
          cnt += recPopped[0]
          ans = max(ans, cnt * recPopped[1])
        s.push((cnt + 1, h))

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().largestRectangleArea(*args), end='\n-----\n')


  test([2, 1, 5, 6, 2, 3])
  test([2, 1, 2])
else:
  print = lambda *args, **kwargs: None
