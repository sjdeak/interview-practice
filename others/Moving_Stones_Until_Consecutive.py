# https://leetcode.com/contest/weekly-contest-134/problems/moving-stones-until-consecutive/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from queue import Queue


def refreshGlobals():
  pass


refreshGlobals()


class Solution(object):
  def numMovesStones(self, a, b, c):
    a, b, c = sorted([a, b, c])
    leftIntervalRange, rightIntervalRange = [b - a, c - b]
    if (leftIntervalRange, rightIntervalRange) == (1, 1):
      return [0, 0]

    maxStep = leftIntervalRange - 1 + rightIntervalRange - 1
    smallIntervalRange = min(leftIntervalRange, rightIntervalRange)
    part = 0
    if smallIntervalRange > 2:
      part = 1
    elif smallIntervalRange == 2:
      part = 0
    else:
      part = 0
    minStep = 1 + part

    return [minStep, maxStep]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().numMovesStones(*args), end='\n-----\n')


  test(1, 2, 5)
  test(4, 3, 2)
  test(3, 5, 1)
  test(4, 7, 1)
else:
  print = lambda *args, **kwargs: None
