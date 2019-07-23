import os
import sys

sys.setrecursionlimit(1000000)


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, P = list(map(int, input().split()))
    forbiddenPrefixes = sorted([input() for i in range(P)], key=len, reverse=True)

    filteredForbiddenPrefixes = []
    for i in range(len(forbiddenPrefixes)):
      for j in range(i + 1, len(forbiddenPrefixes)):
        if forbiddenPrefixes[i].startswith(forbiddenPrefixes[j]):
          break
      else:
        filteredForbiddenPrefixes.append(forbiddenPrefixes[i])

    debug('filteredForbiddenPrefixes:', filteredForbiddenPrefixes)

    ans = 2 ** N
    for px in filteredForbiddenPrefixes:
      ans -= 2 ** (N - len(px))

    print('Case #{}: {}'.format(caseIndex + 1, ans))
