# https://leetcode.com/problems/spiral-matrix/
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

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)  # 右下左上


# 精确地描述行为，以点为单位进行递归，比以层为单位进行递归要好    粒度更小，代码更精炼
class Solution:
  def spiralOrder(self, matrix):  # -> List[int]
    def solve(nowR, nowC, d):
      vis.add((nowR, nowC))
      ans.append(matrix[nowR][nowC])

      for i in range(4):  # 按原有方向一直走到底，除非不能走则换方向
        nowD = (d + i) % 4
        nextR, nextC = nowR + dr[nowD], nowC + dc[nowD]
        if ((nextR, nextC) not in vis) and ((0 <= nextC < column) and (0 <= nextR < row)):
          solve(nextR, nextC, nowD)

    if not matrix or not matrix[0]:
      return []

    row, column = len(matrix), len(matrix[0])
    ans = []
    r, c = 0, 0
    vis = set()
    solve(r, c, 0)

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().spiralOrder(*args), end='\n-----\n')


  test([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ])

  test([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
  ])
  test([[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]])
  test([])
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
