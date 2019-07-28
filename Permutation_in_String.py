# https://leetcode.com/problems/permutation-in-string/
import os
import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(1000000)


# @dump_args
def buildPrefixCounter(S):
  """
  :return 🗳  prefixSumCounter[i] A[:i]的前缀和字符计数器
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


class Solution:
  def checkInclusion(self, s1, s2):  # -> bool
    c1 = Counter(s1)
    pfc = buildPrefixCounter(s2)

    for i in range(0, len(s2) - len(s1) + 1):
      c2 = getCounterDiff(pfc[i], pfc[i + len(s1)])
      if isSameCounter(c1, c2):
        return True

    return False


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().checkInclusion(*args), end='\n-----\n')


  test('ab', 'eidbaooo')
  test('ab', 'eidboaoo')
else:
  print = lambda *args, **kwargs: None
