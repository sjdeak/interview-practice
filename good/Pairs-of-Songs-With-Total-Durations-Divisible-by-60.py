import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter


class Solution:
  def numPairsDivisibleBy60(self, time) -> int:
    if len(time) == 1:
      return 0

    # Note: counter 类似 defaultdict
    ht = Counter(time)

    time.sort()
    # print(time)
    threshold = ceil((time[-2] + time[-1])/60) * 60
    # print('threshold', threshold)

    res = 0
    for a in time:
      for targetSum in range(threshold, 0, -60):
        # print('targetSum', targetSum)
        b = targetSum - a
        if a > b:
          continue

        if ht[b] and a != b:
          # print(f"pair: {a} + {b} = {targetSum}")
          res += ht[b]
        elif ht[b] >= 2 and a == b:
          # print(f"pair: {a} + {b} = {targetSum} * {ht[a]-1}")
          res += ht[b] - 1
      ht[a] -= 1

    return res



if __name__ == '__main__' and ('SJDEAK' in os.environ):
  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().numPairsDivisibleBy60(*args), end='\n-----\n')

  test([30,20,150,100,40])
  test([30,20,150,100,40,30])
  test([60,60,60])
  test([60,60,60,120,120])
  test([30, 60,120,120, 150])
  # test([15,63,451,213,37,209,343,319])
  # test([269,230,318,468,171,158,350,60,287,27,11,384,332,267,412,478,280,303,242,378,129,131,164,467,345,146,264,332,276,479,284,433,117,197,430,203,100,280,145,287,91,157,5,475,288,146,370,199,81,428,278,2,400,23,470,242,411,470,330,144,189,204,62,318,475,24,457,83,204,322,250,478,186,467,350,171,119,245,399,112,252,201,324,317,293,44,295,14,379,382,137,280,265,78,38,323,347,499,238,110,18,224,473,289,198,106,256,279,275,349,210,498,201,175,472,461,116,144,9,221,473])
