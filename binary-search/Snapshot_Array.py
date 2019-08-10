# https://leetcode.com/contest/weekly-contest-148/problems/snapshot-array/
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


class SnapshotArray:

  def __init__(self, length):
    self.his = [[(0, 0)] for i in range(length)]
    self.snapId = 0

  def set(self, index, val):  # -> None
    if self.his[index] and self.his[index][-1][0] == self.snapId:
      self.his[index].pop()

    self.his[index].append((self.snapId, val))

  def snap(self):  # -> int
    self.snapId += 1
    return self.snapId - 1

  def get(self, index, snap_id):  # -> int
    A = self.his[index]
    left, right = 0, len(A) - 1

    # upper_bound
    while left < right:
      print('A, left, right:', A, left, right)
      mid = right - (right - left) // 2
      if A[mid][0] < snap_id:
        left = mid
      elif A[mid][0] > snap_id:
        right = mid - 1
      else:
        return A[mid][1]
    print('left:', left)
    return A[left][1]  # 因为题目保证一定能查到，此处二分不需要最终判断是否合法


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  sa = SnapshotArray(4)

  sa.snap()
  sa.snap()

  sa.set(0, 4)
  sa.snap()
  sa.get(0, 1)
  sa.set(0, 12)
  sa.get(0, 1)
  sa.snap()
  sa.get(0, 3)
  print('sa.get(0,1):', sa.get(0, 1))


else:
  print = lambda *args, **kwargs: None
