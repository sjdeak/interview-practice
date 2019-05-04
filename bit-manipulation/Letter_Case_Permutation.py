# https://leetcode.com/problems/letter-case-permutation/
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


class Solution:
  def letterCasePermutation(self, S):  # -> List[str]
    # 建立alphaMaps: 第i个出现的字符 → 在S中的下标
    # AC后反思 这种实现方法太复杂了，有更简洁的方案
    alphaMaps = []
    for i, ch in enumerate(S):
      if ch.isalpha():
        alphaMaps.append(i)
    print('alphaMaps:', alphaMaps)

    ans = []
    alphaCnt = len(alphaMaps)
    if alphaCnt == 0:
      return [S]

    for sub in range((1 << alphaCnt)):  # 000 001 ... 111
      print('sub, bin(sub), sub.bit_length():', sub, bin(sub), sub.bit_length())

      ls = list(S)
      # for i in range(sub.bit_length()): WA: 0的bit_length是0
      for i in range(alphaCnt):
        print('i:', i)
        if (1 << i) & sub:
          ls[alphaMaps[i]] = ls[alphaMaps[i]].upper()
        else:
          ls[alphaMaps[i]] = ls[alphaMaps[i]].lower()
      ans.append(''.join(ls))

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().letterCasePermutation(*args), end='\n-----\n')


  test("a1b2")
  test("3z4")
  test("12345")
  test("C")
else:
  print = lambda *args, **kwargs: None
