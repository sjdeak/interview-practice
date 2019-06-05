import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter
from operator import itemgetter
from math import sqrt


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')


# 从intervals里选出最多互不相交的区间   所有区间为开区间
def optimalIntervalSelect(intervals):
  pass


# 覆盖[0, L]
def optimalIntervalCover(intervals, L):
  cnt, edNow, tmp = 0, 0, 0

  for i, (left, right) in enumerate(intervals):
    # print('ed: ', ed, 'left: ', left, 'right: ', right, 'tmp: ', tmp)
    if left <= edNow:
      tmp = max(tmp, right)  # 在开始时间早于edNow的区间里 找结束时间最晚的

    if i == len(intervals) - 1 or intervals[i + 1][0] > edNow:
      edNow = tmp
      cnt += 1

    if edNow >= L:
      break

  else:  # 正常退出时 表示无解
    cnt = -1

  return cnt


if __name__ == '__main__':
  for caseIndex in count(1):
    L, G = list(map(int, input().split()))
    if not L and not G: break

    stations = map(lambda t: (t[0] - t[1], t[0] + t[1]),
                   [tuple(map(int, input().split())) for i in range(G)])  # [(x, r),(x, r),...]

    coverCnt = optimalIntervalCover(list(stations), L)
    ans = G - coverCnt if coverCnt != -1 else -1
    print(ans)
