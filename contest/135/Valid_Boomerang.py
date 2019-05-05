# https://leetcode.com/contest/weekly-contest-135/problems/valid-boomerang/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from queue import Queue
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


def getK(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return (y2 - y1) / (x2 - x1) if (x2 - x1) else 'INF'


class Solution:
  def isBoomerang(self, points):  # -> bool
    points = list(map(tuple, points))
    s = set(points)
    if len(s) != len(points):
      return False

    # k1, k2
    p1, p2, p3 = points
    return not (getK(p1, p2) == getK(p2, p3))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().isBoomerang(*args), end='\n-----\n')


  test([[1, 1], [2, 3], [3, 2]])
  test([[1, 1], [2, 2], [3, 3]])
  test([[1, 1], [2, 2], [1, 1]])
  test([[0, 0], [0, 2], [2, 1]])
else:
  print = lambda *args, **kwargs: None
