import os
import sys
from operator import itemgetter

sys.setrecursionlimit(1000000)


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in-small.txt'))
  # sys.stdout = open(os.path.expanduser('./out-small-my.txt'), 'w')

else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func

# 只做小数据
if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, K, P = list(map(int, input().split()))
    refrains = []
    for i in range(K):
      a, b, c = map(int, input().split())
      refrains.append((a - 1, b - 1, c))

    binaryP = bin(P - 1)[2:]
    # debug('binaryP:', binaryP)
    ans = ['0'] * N
    for refrain in refrains:
      ans[refrain[0]] = str(refrain[2])
    refrains = set(map(itemgetter(0), refrains))
    # debug('refrains:', refrains)

    j = N - 1
    for i in range(len(binaryP) - 1, -1, -1):  # 逐位把binaryP填入
      while j in refrains:
        j -= 1
      ans[j] = binaryP[i]
      j -= 1
      # debug('ans:', ans)

    print('Case #{}: {}'.format(caseIndex + 1, ''.join(ans)))
