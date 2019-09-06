# https://leetcode.com/problems/word-search/
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


class Solution:
  def exist(self, board, word):  # -> bool
    def solve(nowR, nowC, st):
      if board[nowR][nowC] != word[st]:
        return False

      # print('nowR, nowC, st, vis:', nowR, nowC, st, vis)
      if st == len(word) - 1:
        return True

      vis.add((nowR, nowC))
      for i in range(4):
        nextR, nextC = nowR + dr[i], nowC + dc[i]
        if ((nextR, nextC) not in vis) and ((0 <= nextC < column) and (0 <= nextR < row)):
          if solve(nextR, nextC, st + 1):
            return True

      vis.remove((nowR, nowC))
      return False

    if not board or not board[0]:
      return []

    row, column = len(board), len(board[0])
    for i in range(row):
      for j in range(column):
        vis = set()
        if solve(i, j, 0):
          return True

    return False


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().exist(*args), end='\n-----\n')


  test([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ], 'ABCCED')
  test([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ], 'SEE')
  test([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ], 'ABCB')

else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
