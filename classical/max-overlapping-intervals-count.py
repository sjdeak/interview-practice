# https://www.nowcoder.com/question/next?pid=16723511&qid=368107&tid=24028391
# solution: https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/
import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter, defaultdict
from operator import itemgetter
from math import sqrt, inf


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  # sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('~/data/out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


# 时间复杂度 O(nlogn)   n: 区间个数
def getMaxOverlappingIntervals(intervals):
  changes = defaultdict(int)
  for interval in intervals:
    st, ed = interval
    changes[st] += 1
    changes[ed] -= 1
  moments = sorted(changes.keys())
  debug('changes:', changes)
  debug('moments:', moments)

  # * 根据changes计算出所有时刻的重叠区间数 * #
  maxCnt = -inf
  maxCntIntervals = []
  curCnt = 0  # 当前时刻的重叠区间数
  preMoment = 0
  for i, curMoment in enumerate(moments):
    if i == 0:
      curCnt += changes[curMoment]
      continue

    preMoment = moments[i - 1]
    # 保证 curCnt = 开区间(preMoment, curMoment)内的重叠区间数

    # region 基于curCnt做一些计算
    if curCnt > maxCnt:
      maxCnt = curCnt
      maxCntIntervals = [(preMoment, curMoment)]
    elif curCnt == maxCnt:
      maxCntIntervals.append((preMoment, curMoment))
    # endregion

    curCnt += changes[curMoment]

  return maxCnt, maxCntIntervals


if __name__ == '__main__':
  N = int(input())
  intervals = [tuple(map(int, input().split())) for i in range(N)]

  maxCnt, maxCntIntervals = getMaxOverlappingIntervals(intervals)
  debug('maxCnt:', maxCnt)
  list(map(lambda t: print(*t), maxCntIntervals))
