import os
import sys
from collections import defaultdict
from functools import lru_cache
from math import *


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
  # debug = lambda *args, **kwargs: None
else:
  debug = lambda *args, **kwargs: None


@lru_cache(None)
def dp(nowAt, nowColor, iVis, visCnt):  # sVis: 序列化后的vis
  # debug('nowAt, nowColor, sVis, visCnt:', nowAt, nowColor, sVis, visCnt)

  if visCnt == K:
    return 0

  choices = []

  # * 回家换衣服 *#
  if nowAt != 0:
    cost = nowAt
    choices += [dp(0, c, 0, visCnt) + cost for c in colors if c != nowColor]

  # * 当前颜色的下一个 *#
  if iVis + 1 <= len(dogs[nowColor]) - 1:
    nextAt = dogs[nowColor][iVis + 1]
    cost = nextAt - nowAt  # 贪心  只往前 到最近的一个
    choices.append(dp(nextAt, nowColor, iVis + 1, visCnt + 1) + cost)

  # debug('choices:', choices)
  res = min(choices or [inf])
  # debug('nowAt, nowColor, sVis, visCnt, ⭐res:', nowAt, nowColor, sVis, visCnt, '⭐', res)
  return res


def serialize(d):
  return tuple(d.items())


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, K = map(int, input().split())
    dists = list(map(int, input().split()))
    colors = list(map(int, input().split()))

    dogs = defaultdict(list)  # color: [dist1, dist2, ...]
    for i, color in enumerate(colors):
      dogs[color].append(dists[i])
    for i, color in enumerate(colors):
      dogs[color] = sorted(dogs[color])
    # debug('dogs:', dogs)

    ans = min([dp(0, c, -1, 0) for c in colors])
    print('Case #{}: {}'.format(caseIndex + 1, ans))
    dp.cache_clear()
