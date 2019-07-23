import os
import sys

sys.setrecursionlimit(1000000)


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')

else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


def solve(n):
  """计算[0,n]里有多少个数满足条件"""


i
if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    L, R = list(map(int, input().split()))
    ans = solve(R) - solve(L)

    print('Case #{}:'.format(caseIndex + 1))
