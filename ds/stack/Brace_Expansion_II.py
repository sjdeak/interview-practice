# https://leetcode.com/contest/weekly-contest-142/problems/brace-expansion-ii/
import os
import sys
from itertools import product

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


# 如果括号字符串非法，返回 False
def bracketsPairs(bracketString, leftBracket='{', rightBracket='}'):
  s = Stack()  # 栈内只存放'('的下标
  ans = []
  for i, ch in enumerate(bracketString):
    if ch == leftBracket:
      s.push(i)
    elif ch == rightBracket:
      if s and bracketString[s.top()] == leftBracket:
        ans.append((s.top(), i))
        s.pop()
      else:
        return False

  return sorted(ans) if not s else False


# 每次只处理一层
def parse(expression) -> set:
  print(f'parsing {expression}')
  if not expression:
    return set()
  length = len(expression)

  pairs = bracketsPairs(expression, '{', '}')
  print('pairs:', pairs)

  # 去除最外层的括号
  if pairs and pairs[0] == (0, length - 1):
    expression = expression[1:-1]
    pairs = bracketsPairs(expression, '{', '}')

  if not ',' in expression and not '{' in expression:  # 例子: 'a'  'ab'
    return {expression}

  tmpExp = []  # 把括号内的字符全部涂成 '#'
  for i in range(len(expression)):
    if any([tp[0] < i < tp[1] for tp in pairs]):
      tmpExp.append('#')
    else:
      tmpExp.append(expression[i])

  print('tmpExp:', tmpExp)

  if ',' in tmpExp:
    tmpExp.append(',')
    pre = 0
    res = set()
    for i, ch in enumerate(tmpExp):
      if ch == ',':
        res |= parse(expression[pre:i])
        pre = i + 1
    print('type2 res:', res)
    return res

  else:  # type 3
    firstPair = pairs[0]

    if firstPair[0] == 0:
      exp1 = expression[:firstPair[1] + 1]
      exp2 = expression[firstPair[1] + 1:]
    else:
      exp1 = expression[:firstPair[0]]
      exp2 = expression[firstPair[0]:]

    print('type3 exp1, exp2:', exp1, exp2)

    set1 = parse(exp1)
    set2 = parse(exp2)

    res = {a + b for (a, b) in product(set1, set2)}
    print('type3 res:', res)
    return res


class Solution:
  def braceExpansionII(self, expression):  # -> List[str]
    return sorted(list(parse(expression)))


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().braceExpansionII(*args), end='\n-----\n')


  test("{a,b}{c{d,e}}")
  test("{{a,z},a{b,c},{ab,z}}")
  test("{a}{a}{a}")
  test("{a,b}c{d,e}f")
  # test("{c{d,e}}")
  # test("{a,b}")
  # test()
else:
  print = lambda *args, **kwargs: None
