# https://leetcode.com/problems/next-greater-element-i/description/
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

  # def empty(self):
  #   return len(self.data) == 0

  def __len__(self):
    return len(self.data)

  def __bool__(self):
    return bool(self.data)


class Solution:
  def nextGreaterElement(self, nums1, nums2):  # -> List[int]
    s = Stack()
    nged = {}  # nextGreaterElement dict
    for i, n in enumerate(nums2[::-1]):
      if not s:
        nged[n] = -1
        s.push(n)
        continue
      while s.top() is not None and s.top() < n:
        s.pop()
      if s.top() is not None:
        nged[n] = s.top()
      else:
        nged[n] = -1
      s.push(n)

    return list(map(nged.__getitem__, nums1))


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().nextGreaterElement(*args), end='\n-----\n')


  test([4, 1, 2], [1, 3, 4, 2])
  test([2, 4], [1, 2, 3, 4])
else:
  print = lambda *args, **kwargs: None
