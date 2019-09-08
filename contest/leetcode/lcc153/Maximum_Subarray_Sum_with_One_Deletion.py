# https://leetcode.com/contest/weekly-contest-153/problems/maximum-subarray-sum-with-one-deletion/
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

"""
dp[i][0/1] 以i结尾的最大连续子数组和 (包含0/1次删除)
"""


class Solution:
  def maximumSum(self, arr):  # -> int
    dp = {}
    for i in range(len(arr)):
      if i == 0:
        dp[i,0] = arr[0]
        dp[i,1] = -inf
        continue

      dp[i, 0] = max(dp[i - 1, 0] + arr[i], arr[i])
      dp[i, 1] = max(dp[i - 1, 0], dp[i - 1, 1] + arr[i])

    print('dp', dp)
    return max([dp[i,j] for i in range(len(arr)) for j in range(2)])


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from utils.linkedlist import ListNode, integerListToListNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maximumSum(*args), end='\n-----\n')


  test([1, -2, 0, 3])
  test([1, -2, -2, 3])
  test([-1, -1, -1, -1])
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
