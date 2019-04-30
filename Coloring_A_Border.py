# https://leetcode.com/contest/weekly-contest-134/problems/coloring-a-border/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from queue import Queue


def refreshGlobals():
  pass


refreshGlobals()

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def dfs(now, A, originalColor, vis):
  vis[now] = True  # 算法保证仅会访问原始颜色=originalColor的块
  nowR, nowC = now

  for i in range(4):
    nextR, nextC = nowR + dx[i], nowC + dy[i]

    if not ((0 <= nextC < len(A[0])) and (0 <= nextR < len(A))):
      continue

    if A[nextR][nextC] == originalColor and (nextR, nextC) not in vis:
      print('nowR, nowC, nextR, nextC', nowR, nowC, nextR, nextC)
      dfs((nextR, nextC), A, originalColor, vis)


class Solution(object):
  def colorBorder(self, grid, r0, c0, color):
    now = (r0, c0)
    vis = {}
    originalColor = grid[r0][c0]
    dyeColor = color

    # 以 now 为起点获取整个连通集
    dfs(now, grid, originalColor, vis)
    # print('vis:', vis)

    borderNodes = set()
    for node in vis:
      nowR, nowC = node
      print('nowR, nowC:', nowR, nowC)

      cnt = 0
      for i in range(4):
        nextR, nextC = nowR + dx[i], nowC + dy[i]

        if not ((0 <= nextC < len(grid[0])) and (0 <= nextR < len(grid))):
          continue
        if grid[nextR][nextC] == originalColor:
          cnt += 1
      print('cnt:', cnt)
      if cnt != 4:
        borderNodes.add((nowR, nowC))

    for node in borderNodes:
      nowR, nowC = node
      grid[nowR][nowC] = dyeColor

    return grid


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().colorBorder(*args), end='\n-----\n')


  test([[1, 1], [1, 2]], 0, 0, 3)
  test([[1, 2, 2], [2, 3, 2]], 0, 1, 3)
  test([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2)






else:
  print = lambda *args, **kwargs: None
