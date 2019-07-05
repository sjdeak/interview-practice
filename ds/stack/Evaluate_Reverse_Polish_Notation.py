# https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/
import os
import sys
from math import *

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
  def evalRPN(self, tokens):  # -> int
    s = Stack()
    for t in tokens:
      if t not in {'+', '-', '*', '/'}:
        s.push(t)
      else:
        n1 = s.pop()
        n2 = s.pop()

        res = eval('{}{}{}'.format(n2, t, n1))
        if t == '/':
          res = ceil(res) if res < 0 else floor(res)

        s.push(str(res))
    return int(s.top())


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().evalRPN(*args), end='\n-----\n')


  test(["2", "1", "+", "3", "*"])
  test(["4", "13", "5", "/", "+"])
  test(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
else:
  print = lambda *args, **kwargs: None
