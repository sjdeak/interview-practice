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

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, O, D = list(map(int, input().split()))  # D: 甜度和限制值 O: 奇数甜度限制个数
    X1, X2, A, B, C, M, L = list(map(int, input().split()))

    print(f'Case #{caseIndex + 1}:')
