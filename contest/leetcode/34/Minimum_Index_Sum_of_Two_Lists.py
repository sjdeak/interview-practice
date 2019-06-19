# https://leetcode.com/contest/leetcode-weekly-contest-34/problems/minimum-index-sum-of-two-lists/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


class Solution:
  def findRestaurant(self, list1, list2):  # -> List[str]
    choices = [(i + j, r1) for i, r1 in enumerate(list1) for j, r2 in enumerate(list2) if r1 == r2]
    minIndexSum = min(choices)[0]
    return list(map(itemgetter(1), filter(lambda c: c[0] == minIndexSum, choices)))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findRestaurant(*args), end='\n-----\n')


  test(["Shogun", "Tapioca Express", "Burger King", "KFC"],
       ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
  test(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
else:
  print = lambda *args, **kwargs: None
