# https://leetcode.com/problems/longest-increasing-subsequence/
import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy

sys.setrecursionlimit(1000000)


class Solution:
  def lengthOfLIS(self, A):  # -> int
    dp = {0: 1}
    help = [0] * (len(A) + 1)

    for i in range(1, len(A)):
      hpi = bisect_left(help, A[i], hi=i + 1) - 1  # 二分出第一个help[l] < A[i]

      dp[i] = hpi + 1  # dp[i] = l + 1
      help[hpi + 1] = max(help[hpi + 1], A[i])  # 更新 help[l + 1]

    print('dp', dp)
    return max([dp[i] for i in range(len(A))])


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().lengthOfLIS(*args), end='\n-----\n')


  test([10, 9, 2, 5, 3, 7, 101, 18])
  # test()
else:
  print = lambda *args, **kwargs: None
