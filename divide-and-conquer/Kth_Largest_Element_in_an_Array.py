# https://leetcode.com/problems/kth-largest-element-in-an-array/
import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1000000)


# 就地
def divideByPivot(A, l, r):
  while l < r:
    print('l,r:', l, r)
    while A[r] >= A[l] and l != r:  # A[l]为pivot
      r -= 1
    A[l], A[r] = A[r], A[l]
    while A[l] <= A[r] and l != r:  # A[r]为pivot
      l += 1
    A[l], A[r] = A[r], A[l]

  print('res pivotI:', l)
  return l


class Solution:
  # 不就地 每一次调用时的nums都是独立的
  def findKthLargest(self, nums, k):  # -> int
    print('nums, k:', nums, k)

    if len(nums) == 1:
      return nums[0]

    pivotI = divideByPivot(nums, 0, len(nums) - 1)
    if pivotI == len(nums) - k:
      return nums[pivotI]
    elif pivotI > len(nums) - k:
      return self.findKthLargest(nums[:pivotI], k - (len(nums) - 1 - pivotI + 1))
    else:
      return self.findKthLargest(nums[pivotI + 1:], k)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findKthLargest(*args), end='\n-----\n')


  test([3, 2, 1, 5, 6, 4], 2)
  test([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
else:
  print = lambda *args, **kwargs: None
