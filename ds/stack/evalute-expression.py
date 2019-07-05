import unittest


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


def evalRPN(tokens):  # -> int
  s = Stack()
  for t in tokens:
    if t not in {'+', '-', '*', '/'}:
      s.push(t)
    else:
      n1 = s.pop()
      n2 = s.pop()

      res = eval(f'{n2}{t}{n1}')

      s.push(str(res))
  return int(s.top())


# 调度场算法  原理未知

def infixToRPN(tokens):  # -> int
  s = Stack()
  priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

  res = []
  for t in tokens:
    if t == '(':
      s.push(t)
    elif t == ')':  # 处理到上一个'('为止d
      while s and s.top() != '(':
        res.append(s.pop())
      if s and s.top() == '(':
        s.pop()
    elif t in {'+', '-', '*', '/'}:
      while s and priority[s.top()] > priority[t]:  # 例子: 栈内'*' t='+'
        res.append(s.pop())
      s.push(t)
    else:
      res.append(t)

  while s:
    res.append(s.pop())

  return res


class Test(unittest.TestCase):

  def test(self):
    self.assertEqual(['1', '2', '+', '3', '*'], infixToRPN(['(', '1', '+', '2', ')', '*', '3']))


if __name__ == "__main__":
  unittest.main()
