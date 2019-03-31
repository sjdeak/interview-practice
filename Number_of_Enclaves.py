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


# 以 now 为起点进行连通集探索
def dfs(now, A, group, vis):
  vis[now] = True  # 打卡
  nowR, nowC = now
  for i in range(4):
    nextR, nextC = nowR + dx[i], nowC + dy[i]

    if not ((0 <= nextC < len(A[0])) and (0 <= nextR < len(A))):
      group.add('canWalkOff')
      continue

    if A[nextR][nextC] == 1 and not vis[(nextR, nextC)]:
      print('nowR, nowC, nextR, nextC', nowR, nowC, nextR, nextC)
      group.add((nextR, nextC))
      dfs((nextR, nextC), A, group, vis)


class Solution:
  def numEnclaves(self, A):  # -> int
    sets = []
    vis = defaultdict(bool)  # 判重用哈希表
    R, C = len(A), len(A[0])
    for r in range(R):
      for c in range(C):
        if A[r][c] and not vis[(r, c)]:
          group = {(r, c)}
          sets.append(group)
          dfs((r, c), A, group, vis)

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
