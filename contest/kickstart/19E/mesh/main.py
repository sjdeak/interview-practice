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


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdin = open(os.path.expanduser('./in2.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


# template getConnectSets
def getConnectSets(graph, nodes):  # -> {'连通集中的一个节点': 该连通集里所有节点组成的set}
  def dfs(u, belongTo):
    vis.add(u)
    connectSets[belongTo].add(u)
    for v in graph[u]:
      if v not in vis:
        dfs(v, belongTo)

  connectSets = defaultdict(set)
  vis = set()
  for node in nodes:
    if node not in vis:
      dfs(node, node)

  return connectSets


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, M = list(map(int, input().split()))
    graph = defaultdict(list)
    nodes = set()
    for i in range(M):
      u, v = list(map(lambda s: int(s) - 1, input().split()))
      graph[u].append(v)
      graph[v].append(u)
      nodes.add(u)
      nodes.add(v)
    # /* 求各个黑连通集的数目 */

    connectSets = getConnectSets(graph, nodes)
    debug('connectSets:', connectSets)

    ans = 0
    blackCnt = 0
    for cs in connectSets.values():
      ans += len(cs) - 1  # 各个黑连通集内部的
      blackCnt += len(cs)

    redCnt = N - blackCnt
    blackSetCnt = len(connectSets.values())
    ans += (blackSetCnt + redCnt - 1) * 2

    print('Case #{}: {}'.format(caseIndex + 1, ans))
