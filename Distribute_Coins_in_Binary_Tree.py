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

def preorderTraversal(node, func):
  if not node:
    return
  func(node)
  preorderTraversal(node.left, func)
  preorderTraversal(node.right, func)

def bfsTraversal(root, func):
  q = Queue()
  q.put(root)

  while not q.empty():
    now = q.get()
    if not now:
      continue
    func(now)
    q.put(now.left)
    q.put(now.right)


def move(a, b, direction, nodes, step):
  a.val += direction
  b.val -= direction
  dfs(nodes, step + 1)
  a.val -= direction
  b.val += direction


ans = 10 ** 10
nodes = []
ignoredups = set()

def dfs(nodes, step):
  coins = []
  bfsTraversal(nodes[0], lambda n: coins.append(n.val)) # todo 一下子写太多了，分块测试

  tcoins = tuple(coins)
  if tcoins in ignoredups:
    return
  else:
    ignoredups.add(tcoins)

  if step > ans: # 最优性剪枝
    return

  if all([c == 1 for c in coins]):
    if step < ans:
      ans = step
    return

  for nd in nodes:
    if nd.val:
      if nd.left:
        move(nd, nd.left, 1, nodes, step)
        move(nd, nd.left, -1, nodes, step)
      if nd.right:
        move(nd, nd.right, 1, nodes, step)
        move(nd, nd.right, -1, nodes, step)


class Solution:
  def distributeCoins(self, root) -> int:
    bfsTraversal(root, lambda nd: nodes.append(nd))
    dfs(nodes, 0)
    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().distributeCoins(*args), end='\n-----\n')


    test()
    test()
