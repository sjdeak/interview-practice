# https://leetcode.com/contest/leetcode-weekly-contest-34/problems/non-negative-integers-without-consecutive-ones/
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


# 此dp回答n位长, 首位为b的数里间有多少个不包含连续1的
@lru_cache(None)
def auxDp(n, b):
  if n == 1:
    return 1

  if b == 1:
    return auxDp(n - 1, 0)
  elif b == 0:
    return auxDp(n - 1, 0) + auxDp(n - 1, 1)


@lru_cache(None)
def mainDp(num):
  if num == 0:
    return 1
  elif num == 1:
    return 2

  bitLength = num.bit_length()
  aux = auxDp(bitLength, 0)

  num = ((1 << (bitLength - 2)) - 1) & num  # 用001111..11来&num
  main = mainDp(num)
  # print(f'auxDp({bitLength}, 0):', aux)
  # print(f'mainDp({num}):', main)
  return aux + main


class Solution:
  def findIntegers(self, num):  # -> int
    return mainDp(num)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findIntegers(*args), end='\n-----\n')


  # print('auxDp(3,0):', auxDp(3, 0))
  test(5)
  test(3)


else:
  print = lambda *args, **kwargs: None
