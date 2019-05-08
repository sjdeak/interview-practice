# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


class Solution:
  def shortestPathLength(self, graph):
    return self.shortestPathLengthDP(graph)

  # while形式的dp
  def shortestPathLengthDP(self, graph):
    length = len(graph)
    dp = defaultdict(lambda: float('inf'))
    dp.update({(1 << x, x): 0 for x in range(length)})
    print('dp:', dp)

    for x in range(length):
      queue = deque([(1 << x, x)])
      while queue:
        now = queue.popleft()
        cover, head = now

        for v in graph[head]:
          cover2 = cover | (1 << v)
          if dp[now] + 1 < dp[cover2, v]:
            queue.append((cover2, v))
          dp[cover2, v] = min(dp[cover2, v], dp[now] + 1)

    print('dp:', dp)
    return min(dp[(1 << length) - 1, x] for x in range(length))

  def shortestPathLengthBFS(self, graph):  # BFS版
    length = len(graph)
    queue = deque((1 << x, x) for x in range(length))
    dist = defaultdict(lambda: length * length)

    while queue:
      cover, head = queue.popleft()
      d = dist[cover, head]
      if cover == (1 << length) - 1:
        return d
      for v in graph[head]:
        cover2 = cover | (1 << v)
        if d + 1 < dist[cover2, v]:  # 防止走回头路
          dist[cover2, v] = d + 1
          queue.append((cover2, v))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().shortestPathLength(*args), end='\n-----\n')


  test([[1, 2, 3], [0], [0], [0]])
  test([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
else:
  print = lambda *args, **kwargs: None
