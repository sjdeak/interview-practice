# https://leetcode.com/problems/insert-interval/
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


# template 多个区间合并
def merge(intervals):  # -> List[List[int]]
  """ demo doctest
  >>> merge([[1,3],[2,6],[8,10],[15,18]])
  [[1, 6], [8, 10], [15, 18]]
  """

  if not intervals:
    return []

  intervals.sort()
  ans = []
  st, ed = intervals[0]

  for i, (l1, r1) in enumerate(intervals[:-1]):
    l2, r2 = intervals[i + 1]
    if l2 <= ed:
      ed = max(r2, ed)
    else:  # 不相交
      ans.append([st, ed])
      st, ed = l2, r2

  # 主循环里只有遇到下一个不相交的区间时才会 append ans
  # 所以需要额外处理最后一个区间  有两种情况 1. 和前一个区间合并了 2. 没有合并
  ans.append([st, ed])

  return ans


class Solution:
  def insert(self, intervals, newInterval):  # -> List[List[int]]
    intervals.append(newInterval)
    return merge(intervals)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().insert(*args), end='\n-----\n')


  test([[1, 3], [6, 9]], [2, 5])
  test([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
