# https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


class Solution:
  def findMin(self, nums):  # -> int

    pass


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findMin(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
