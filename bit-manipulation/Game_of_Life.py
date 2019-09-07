# https://leetcode.com/problems/game-of-life/
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
  def gameOfLife(self, board):  # -> None
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
      return board
    rowCnt, columnCnt = len(board), len(board[0])
    for nowR in range(rowCnt):
      for nowC in range(columnCnt):

        liveCnt, deadCnt = 0, 0
        # template 八连通块
        for dr in range(-1, 2):
          for dc in range(1, -2, -1):
            if dr == 0 and dc == 0:
              continue
            nextR, nextC = nowR + dr, nowC + dc
            if 0 <= nextR < rowCnt and 0 <= nextC < columnCnt:
              if 1 & board[nextR][nextC]:
                liveCnt += 1
              else:
                deadCnt += 1

        currentState = 1 & board[nowR][nowC]
        if currentState == 1:
          nextState = int(liveCnt in [2, 3])
        else:
          nextState = int(liveCnt == 3)

        print('nowR, nowC, currentState, nextState:', nowR, nowC, currentState, nextState)

        val = 0
        # 0b nextState currentState
        board[nowR][nowC] = val | (nextState << 1) | currentState

        print('board[nowR][nowC]:', bin(board[nowR][nowC]))

    for nowR in range(rowCnt):
      for nowC in range(columnCnt):
        board[nowR][nowC] = int(bool((1 << 1) & board[nowR][nowC]))
        # board[nowR][nowC] = (2 & board[nowR][nowC]) >> 1

    # return board


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().gameOfLife(*args), end='\n-----\n')


  test([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
  ])
  # test()
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
