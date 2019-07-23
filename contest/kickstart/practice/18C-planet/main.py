import os
import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


# 输入保证图中只有一个环
def findCircle(graph):
  # print('graph', graph)
  def _dfs(u: int, footprint: list):
    # print('u, footprint:', u, footprint)
    footprint.append(u)
    # print('graph[u]:', graph[u])
    for v in graph[u]:
      if len(footprint) >= 2 and footprint[-2] == v:  # 防止走回头
        continue
      if v in footprint:
        return footprint[footprint.index(v):]
      else:
        return _dfs(v, footprint)

  if graph.keys():
    return _dfs(tuple(graph.keys())[0], [])
  else:
    return -1


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    edges = [tuple(map(int, input().split())) for i in range(int(input()))]
    graph = defaultdict(list)
    for u, v in edges:
      graph[u - 1].append(v - 1)
      graph[v - 1].append(u - 1)

    print('Case #{}:'.format(caseIndex + 1))
    debug(findCircle(graph))
