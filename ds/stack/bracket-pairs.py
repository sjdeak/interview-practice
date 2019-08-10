import os


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  # sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


# 🗳  stack
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


# 如果括号字符串非法，返回 False
def bracketsPairs(bracketString):
  s = Stack()  # 栈内只存放'('的下标
  ans = []
  for i, ch in enumerate(bracketString):
    if ch == ')':
      if s.top() is not None and bracketString[s.top()] == '(':
        ans.append((s.top(), i))
        s.pop()
      else:
        return False
    else:
      s.push(i)

  return ans if not s else False


if __name__ == '__main__':
  print("bracketsPairs('(())'):", bracketsPairs('(())'))
  print("bracketsPairs('()()'):", bracketsPairs('()()'))
  print("bracketsPairs('()('):", bracketsPairs('()('))
