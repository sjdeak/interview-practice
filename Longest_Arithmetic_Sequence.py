# https://leetcode.com/contest/weekly-contest-132/problems/longest-arithmetic-sequence/
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


class Solution:
  def longestArithSeqLength(self, A):  # -> int
    table = {}
    length = len(A)
    for j in range(length):
      minusDict = {}
      for i in range(j - 1, -1, -1):
        minus = A[j] - A[i]
        if minus not in minusDict:
          minusDict[minus] = i

      table[j] = {
        'minus': sorted(list(minusDict.keys())),
        'minusDict': minusDict
      }
    print('table:', table)

    dp = {}
    ans = 1

    for i in range(1, length):
      for d in table[i]['minus']:
        minusDict = table[i]['minusDict']
        j = minusDict[d]

        if (j, d) not in dp:
          dp[(i, d)] = 2
        else:
          dp[(i, d)] = dp[(j, d)] + 1
        ans = max(dp[(i, d)], ans)

    print('dp', dp)
    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().longestArithSeqLength(*args), end='\n-----\n')


  test([3, 6, 9, 12])
  test([9, 4, 7, 2, 10])
  test([20, 1, 15, 3, 10, 5, 8])
  test(
    [44, 46, 22, 68, 45, 66, 43, 9, 37, 30, 50, 67, 32, 47, 44, 11, 15, 4, 11, 6, 20, 64, 54, 54, 61, 63, 23, 43, 3, 12,
     51, 61, 16, 57, 14, 12, 55, 17, 18, 25, 19, 28, 45, 56, 29, 39, 52, 8, 1, 21, 17, 21, 23, 70, 51, 61, 21, 52, 25,
     28])
else:
  print = lambda *args, **kwargs: None
