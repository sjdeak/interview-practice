# https://leetcode.com/problems/3sum/
import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1000000)


def twoSum(A, tar, st=0):
  """
  并不能返回所有符合条件的下标对，只保证返回的下标对对应的值对是没有遗漏的
  :param A:
  :param tar:
  :param st: 从A[st:]里找
  :return: List[List[int]] 所有和为tar的下标对
  """
  left, right = st, len(A) - 1
  res = []
  while left < right:
    # 左右指针不断逼近，直至找到一组解 #
    while (A[left] + A[right] < tar or left == ignore) and left < right:
      left += 1
    while (A[left] + A[right] > tar or right == ignore) and left < right:
      right -= 1

    if A[left] + A[right] == tar and left < right:
      res.append([left, right])
      lNum, rNum = A[left], A[right]
      # 尽可能快速地缩小[left, right] #
      while A[left] == lNum and left < right:
        left += 1
      while A[right] == rNum and left < right:
        right -= 1

  return res


def twoSumOld(A, tar, ignore=None):
  """
  并不能返回所有符合条件的下标对，只保证返回的下标对对应的值对是没有遗漏的
  :param A:
  :param tar:
  :param ignore: 要无视的下标 (就好像A中没有这个元素)
  :return: List[List[int]] 所有和为tar的下标对
  """
  left, right = 0, len(A) - 1
  res = []
  while left < right:
    # 左右指针不断逼近，直至找到一组解 #
    while (A[left] + A[right] < tar or left == ignore) and left < right:
      left += 1
    while (A[left] + A[right] > tar or right == ignore) and left < right:
      right -= 1

    if A[left] + A[right] == tar and left < right:
      res.append([left, right])
      lNum, rNum = A[left], A[right]
      # 避免重复解(下标对应的值对相同)
      while A[left] == lNum and left < right:
        left += 1
      while A[right] == rNum and left < right:
        right -= 1

  return res


class Solution:
  def threeSum(self, nums):  # -> List[List[int]]
    nums.sort()
    ans = []
    for i, num in enumerate(nums):  # 枚举3Sum结果中下标最小的一项  twoSumOld用ignore不如用st，同样满足题意，而且更方便
      twoSumRes = twoSumOld(nums, -num, i)  # O(n)
      ans.extend([[i] + r for r in twoSumRes if r[0] > i])

    for i, triplet in enumerate(ans):
      ans[i] = list(map(lambda i: nums[i], triplet))

    ans = set(map(tuple, ans))
    ans = list(map(list, list(ans)))
    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().threeSum(*args), end='\n-----\n')


  test(sorted([-1, 0, 1, 2, -1, -4]))
  # test([-1, 0, 1, 2, -1, -4])
  # test()
else:
  print = lambda *args, **kwargs: None
