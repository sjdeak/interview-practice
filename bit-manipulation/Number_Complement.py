# https://leetcode.com/problems/number-complement/
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
  def findComplement(self, num):
    # 找比num大的最靠近num的2的阶乘数
    target = 1
    for k in range(0, 32):
      if (1 << k) > num:
        target = 1 << k
        break

    return num ^ (target - 1)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findComplement(*args), end='\n-----\n')


  test(5)
  test(1)
else:
  print = lambda *args, **kwargs: None
