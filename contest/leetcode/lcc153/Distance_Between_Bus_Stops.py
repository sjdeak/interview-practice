# https://leetcode.com/contest/weekly-contest-153/problems/distance-between-bus-stops/
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


class Solution:
  def distanceBetweenBusStops(self, distance, start, destination):  # -> int
    # 只考虑顺时针走

    if start <= destination:
      dist = sum(distance[start:destination])
    else:
      dist = sum(distance[start:]) + sum(distance[:destination])

    print('dist:', dist)
    return min(dist, sum(distance)-dist)




if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from utils.linkedlist import ListNode, integerListToListNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().distanceBetweenBusStops(*args), end='\n-----\n')


  test([1,2,3,4], 0, 1)
  test([1,2,3,4], 0, 2)
  test([1,2,3,4], 0, 3)
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
