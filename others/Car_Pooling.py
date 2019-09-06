# https://leetcode.com/contest/weekly-contest-142/problems/car-pooling/
import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1000000)


# 时间复杂度 O(nlogn)   n: 区间个数
def getMaxOverlappingIntervals(intervals):
  changes = defaultdict(int)
  for interval in intervals:
    cnt, st, ed = interval
    changes[st] += cnt
    changes[ed] -= cnt
  moments = sorted(changes.keys())
  print('changes:', changes)
  print('moments:', moments)

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

  print('maxCnt:', maxCnt)

  return maxCnt, maxCntIntervals


class Solution:
  def carPooling(self, trips, capacity):  # -> bool
    maxCnt, maxCntIntervals = getMaxOverlappingIntervals(trips)
    return maxCnt <= capacity


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().carPooling(*args), end='\n-----\n')


  test([[2, 1, 5], [3, 3, 7]], 4)
  test([[2, 1, 5], [3, 3, 7]], 5)
  test([[2, 1, 5], [3, 5, 7]], 3)
  test([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11)
else:
  print = lambda *args, **kwargs: None
