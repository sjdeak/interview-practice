# https://leetcode.com/problems/min-stack/
import os
import sys

sys.setrecursionlimit(1000000)


class MinStack:

  def __init__(self):
    """
    initialize your data structure here.
    """
    self.data = []
    self.his = []

  def push(self, x):  # -> None
    self.data.append(x)
    self.his.append(min(self.his[-1], x) if len(self.his) else x)

  def pop(self):  # -> None
    self.his.pop()
    self.data.pop()

  def top(self):  # -> item on top
    return self.data[-1] if len(self.data) else None

  def getMin(self):  # -> int
    return self.his[-1]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  obj = MinStack()
  obj.push(-2)
  obj.push(0)
  obj.push(-3)
  print('obj.getMin():', obj.getMin())
  obj.pop()
  print('obj.top():', obj.top())
  print('obj.getMin():', obj.getMin())
