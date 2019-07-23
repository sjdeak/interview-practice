import os
import sys


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    R, C, K = map(int, input().split())
    thickness = [list(map(int, input().split())) for r in range(R)]
