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


# 以now为起点进行连通集探索
def dfs(now, A, group, vis):
  vis[now] = True  # 打卡
  nx, ny = now
  for i in range(4):
    x, y = nx + dx[i], ny + dy[i]

    if not ((0 <= y < len(A[0])) and (0 <= x < len(A))):
      group.add('canWalkOff')
      continue

    if A[x][y] == 1 and not vis[(x, y)]:
      print('nx, ny, x, y', nx, ny, x, y)
      group.add((x, y))
      dfs((x, y), A, group, vis)


class Solution:
  def numEnclaves(self, A):  # -> int
    sets = []
    vis = defaultdict(bool)
    for i in range(len(A)):
      for j in range(len(A[0])):
        if A[i][j] and not vis[(i, j)]:
          group = {(i, j)}
          sets.append(group)
          dfs((i, j), A, group, vis)

    ans = 0
    for s in sets:
      if not 'canWalkOff' in s:
        ans += len(s)

    print('sets', sets)

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().numEnclaves(*args), end='\n-----\n')


  test([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
  test([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
  test([[0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]])
else:
  print = lambda *args, **kwargs: None
