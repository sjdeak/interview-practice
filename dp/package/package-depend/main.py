import os
import sys
from collections import namedtuple, defaultdict
from math import *


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


def zeroOnePackage(items, volume):
  subDP = defaultdict(int)
  length = len(items)
  ans = -inf
  # subDP[i,vol] 从前i种物品里选，必须把背包装到容量为vol，这时可得到的最大价值
  # 教训: i为几就指向第i种物品  哪怕这样需要对i=0时做预处理  也不要把下标搞乱  KISS
  for i in range(length):
    for s in range(1, volume + 1):  # s: size
      if items[i].vol <= s:
        subDP[(i, s)] = max(subDP[i - 1, s], subDP[i - 1, s - items[i].vol] + items[i].val)
      else:
        subDP[(i, s)] = subDP[i - 1, s]
      ans = max(ans, subDP[(i, s)])

  # debug('subDP', subDP)
  return ans


def dfs(u):
  # dp[u, vol]: 从节点u开始取，背包最大体积为v，这时能得到的最大价值
  for child in graph[u]:
    dfs(child)

  choices = [0]  # 什么都不取
  if Volume > items[u].vol:
    choices.append(items[u].val)  # 只取u

  # 取u以及u的子件  看做嵌套了一个01背包问题来处理
  A = list(map(lambda i: items[i], graph[u]))
  subRes = zeroOnePackage(A, Volume - items[u].val)
  choices.append(items[u].val + subRes)

  dp[u, vol] = max(choices)

  debug('dp:', *sorted(dp.items()), sep='\n')


if __name__ == '__main__':
  N, Volume = list(map(int, input().split()))
  # 把par的下标转成从0开始
  items = [namedtuple('item', ['vol', 'val', 'par'])(
    *(lambda l: [n - 1 if i == 2 and n != -1 else n for i, n in l])(map(int, input().split()))) for
    i in range(N)]
  graph = defaultdict(list)
  root = None
  for i, item in enumerate(items):
    if item.par == -1:
      root = i
      continue
    graph[item.par].append(i)

  dp = defaultdict(int)
  dfs(root)
