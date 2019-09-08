# https://leetcode.com/contest/weekly-contest-153/problems/day-of-the-week/
import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy
from datetime import date

sys.setrecursionlimit(1000000)


class Solution:
  def dayOfTheWeek(self, day, month, year):  # -> str
    dt = date(year, month, day)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[dt.weekday()]



if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from utils.linkedlist import ListNode, integerListToListNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().dayOfTheWeek(*args), end='\n-----\n')


  test(31, 8, 2019)
  # test()
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
