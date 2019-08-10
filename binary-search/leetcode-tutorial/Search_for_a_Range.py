# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
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
from bisect import bisect_left, bisect_right


def refreshGlobals():
  pass


refreshGlobals()


class Solution(object):
  def searchRange(self, nums, target):
    if not nums:
      return [-1, -1]
    li, ri = bisect_left(nums, target), bisect_right(nums, target)
    print('li, ri:', li, ri)

    if li > len(nums) - 1 or nums[li] != target:
      return [-1, -1]
    else:
      return [li, ri - 1]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().searchRange(*args), end='\n-----\n')


  test([5, 7, 7, 8, 8, 10], 8)
  test([5, 7, 7, 8, 8, 10], 6)
  test([5, 7, 7, 8, 10], 8)
  test([2, 2], 3)
else:
  print = lambda *args, **kwargs: None
