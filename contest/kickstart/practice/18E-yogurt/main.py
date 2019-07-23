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
    N, K = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))

    cnt = 0
    now = 0  # 当前过了几天
    i = 0
    k = 0

    while i < len(A):
      if A[i] > now:
        k += 1  # 喝掉一杯
        cnt += 1
        i += 1
      else:
        i += 1  # 跳过变质的

      if k == K:
        k = 0
        now += 1  # 增加一天

    print(f'Case #{caseIndex + 1}: {cnt}')
