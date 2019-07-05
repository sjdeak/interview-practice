import os
import sys


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open('../../../icpc-data/in.txt')
  # sys.stdout = open(os.path.expanduser('~/data/out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, Q = map(int, input().split())
    S = input()

    sets = [set(), ]  # S[:i]里出现奇数次的字符
    for i, ch in enumerate(S):
      s = set(sets[i])
      if ch in s:
        s.remove(ch)
      else:
        s.add(ch)

      sets.append(s)

    # print('sets:', sets)

    ans = 0
    for _ in range(Q):
      l, r = map(int, input().split())
      diff = sets[r - 1 + 1] ^ sets[l - 1]
      if len(diff) <= 1:
        # print('l,r,diff:', l, r, diff)
        ans += 1

    print("Case #{}: {}".format(caseIndex + 1, ans))
