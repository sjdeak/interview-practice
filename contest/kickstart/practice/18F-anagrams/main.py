import os
import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')

else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


# @dump_args
def buildPrefixCounter(S):
  """
  :return prefixSumCounter[i] A[:i]的前缀和字符计数器
  """
  d = defaultdict(int)
  prefixSumCounter = [d]
  for ch in S:
    d = d.copy()
    d[ch] += 1
    prefixSumCounter.append(d)
  return prefixSumCounter


# @dump_args
def getCounterDiff(c1, c2):  # c2 包含 c1
  c = c2.copy()
  for ch in c1:
    c[ch] -= c1[ch]
  return c


# @dump_args
def isSameCounter(c1, c2):
  return all([c2[ch] == c1[ch] for ch in c1]) and all([c2[ch] == c1[ch] for ch in c2])


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    L = int(input())
    S1 = input()
    S2 = input()
    counterS1 = buildPrefixCounter(S1)
    counterS2 = buildPrefixCounter(S2)

    sub2Counters = defaultdict(list)
    for length in range(1, L + 1):
      for j in range(0, L - length + 1):
        sub2Counters[length].append(getCounterDiff(counterS2[j], counterS2[(j + length - 1) + 1]))

    ans = 0
    # 复杂度分析: 50
    for length in range(1, L + 1):
      # 复杂度分析: 50
      for i in range(0, L - length + 1):
        # 复杂度分析: 最坏情况下 26*2
        sub1Counter = getCounterDiff(counterS1[i], counterS1[(i + length - 1) + 1])  # 枚举出所有子串的counter

        # debug('sub1Counter:', sub1Counter)

        try:
          for sub2Counter in sub2Counters[length]:
            # 复杂度分析: 最坏情况下 26*2
            if isSameCounter(sub1Counter, sub2Counter):
              # debug('sub1Counter, sub2Counter:', sub1Counter, sub2Counter)
              raise CustomException
        except CustomException:
          ans += 1
    # 总复杂度: 50*50*52*52 ~ 6.25*10^6
    print('Case #{}: {}'.format(caseIndex + 1, ans))
