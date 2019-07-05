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


def groupPackage(items, volume, weight):
  dp = defaultdict(int)  # 滚动数组对内存的优化极其巨大 后续可以考虑开始用了  特别是N很大的场景
  length = len(items)
  ans = -inf
  # dp[i,vol,wei] 从前i种物品里选，必须把背包装到容量为vol、重量为wei，这时可得到的最大价值
  for i in range(length):
    for v in range(1, volume + 1):
      for w in range(1, weight + 1):
        if items[i].vol <= v and items[i].wei <= w:
          dp[(i, v, w)] = max(dp[i - 1, v, w], dp[i - 1, v - items[i].vol, w - items[i].wei] + items[i].val)
        else:
          dp[(i, v, w)] = dp[i - 1, v, w]
        ans = max(ans, dp[(i, v, w)])

  # debug('dp', dp)
  return ans


if __name__ == '__main__':
  N, Volume, Weight = list(map(int, input().split()))
  items = [namedtuple('item', ['vol', 'wei', 'val'])(*map(int, input().split())) for i in range(N)]

  print(groupPackage(items, Volume, Weight))
