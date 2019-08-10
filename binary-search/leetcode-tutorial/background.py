# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from bisect import bisect_left, bisect_right
from queue import Queue


def refreshGlobals():
  pass


refreshGlobals()


class Solution:
  def search(self, nums, target):  # -> int
    i = bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().search(*args), end='\n-----\n')


  test([-1, 0, 3, 5, 9, 12], 9)
  test([-1, 0, 3, 5, 9, 12], 2)
  test([-1, 0, 3, 5, 9, 12], -2)
  test([-1, 0, 3, 5, 9, 12], 13)
else:
  print = lambda *args, **kwargs: None
