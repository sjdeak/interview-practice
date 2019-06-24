# https://leetcode.com/problems/reverse-pairs/solution/
import operator
import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1000000)


# 复杂度 O(nlog^2n)
# WA但通过大部分用例
def mergeAndCountReversePair(A1, A2, cmp=operator.lt):
  i1, i2 = 0, 0
  len1, len2 = len(A1), len(A2)
  res = []
  cnt = 0  # A1, A2间相对的逆序对数
  while i1 < len1 or i2 < len2:
    n1, n2 = A1[i1] if i1 != len1 else inf, A2[i2] if i2 != len2 else inf
    if cmp(n1, n2):
      res.append(n1)
      i1 += 1
      # cnt += i2
      idx = bisect_left(A2, n1 / 2, hi=i2)
      cnt += idx
    else:
      res.append(n2)
      i2 += 1

  return cnt, res


# 返回 (逆序对数, 排序好的A)
def getReversePairCount(A):
  # * 特判 *#
  if len(A) <= 1:
    return 0, A
  # * 归 *#
  half = len(A) // 2
  cnt1, A1 = getReversePairCount(A[:half])
  cnt2, A2 = getReversePairCount(A[half:])
  # * 并 #
  cnt3, A3 = mergeAndCountReversePair(A1, A2)
  return cnt1 + cnt2 + cnt3, A3


class Solution:
  def reversePairs(self, nums):  # -> int
    cnt, A = getReversePairCount(nums)
    return cnt


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().reversePairs(*args), end='\n-----\n')


  test([1, 3, 2, 3, 1])
  test([2, 4, 3, 5, 1])
else:
  print = lambda *args, **kwargs: None
