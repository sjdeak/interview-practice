# https://leetcode.com/contest/weekly-contest-134/problems/uncrossed-lines/
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
  def maxUncrossedLines(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    dp = {(i, 0): 0 for i in range(len(A) + 1)}
    for j in range(len(B) + 1):
      dp[(0, j)] = 0

    # dp[i,j]: A[:i] B[:j] 上的ans
    for i in range(1, len(A) + 1):
      for j in range(1, len(B) + 1):
        choices = []
        if A[i - 1] == B[j - 1]:
          choices.append(1 + dp[i - 1, j - 1])
        choices.append(dp[i - 1, j])
        choices.append(dp[i, j - 1])
        dp[i, j] = max(choices)

    # print('dp', dp)
    return dp[len(A), len(B)]


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxUncrossedLines(*args), end='\n-----\n')


  test([1, 4, 2], [1, 2, 4])
  test([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])
  test([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1])
else:
  print = lambda *args, **kwargs: None
