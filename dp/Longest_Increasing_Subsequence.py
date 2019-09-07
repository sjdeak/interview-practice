# https://leetcode.com/problems/longest-increasing-subsequence/
# https://www.acwing.com/solution/LeetCode/content/287/
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


# 真正的LIS 子串不要求连续
# 不能用单调栈做，上升子串中A[i]的下一项未必是他的nextGreaterElement  A = [1, 4, 2, 5], 求以5结尾的LIS
class Solution:
  def lengthOfLIS(self, A):  # -> int
    if not A:
      return 0

    help = [inf] * (len(A) + 1)
    help[1] = A[0]  # {上升子序列长度: 最小的结尾num值}  help一定单调递增
    maxLen = 1  # 当前(遍历到i之前)能找到的最长上升子串的长度

    for i in range(1, len(A)):
      # 找第一个help[j] < A[i]
      bsi = bisect_left(help, A[i], lo=1, hi=maxLen + 1)
      # print('raw bsi:', bsi)
      j = bsi - 1 if bsi != 1 else 0  # 这里的j就是acwing题解里要找的那个j
      help[j + 1] = min(help[j + 1], A[i])
      if j + 1 > maxLen:
        maxLen = j + 1
    print('help:', help)

    return maxLen


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().lengthOfLIS(*args), end='\n-----\n')


  test([1, 2])
  test([10, 9, 2, 5, 3, 7, 101, 18])
else:
  print = lambda *args, **kwargs: None
