# https://leetcode.com/problems/maximum-product-of-word-lengths/
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


def refreshGlobals():
  pass


refreshGlobals()


# print('toBits("abc"):', bin(toBits("abc")))

# 时间复杂度 O(len(s1)+len(s2)) 空间复杂度 O(1)
def hasSameCh(s1, s2):
  def toBits(s):
    res = 0
    for ch in s:
      res |= 1 << (ord(ch) - ord('a'))
    return res

  ans = toBits(s1) & toBits(s2)
  # print('s1, s2, ans:', s1, s2, ans)
  return ans


def toBits(s):
  res = 0
  for ch in s:
    res |= 1 << (ord(ch) - ord('a'))
  return res


class Solution:
  # 依靠位运算 时间复杂度才能降到 O(n^2)
  def maxProduct(self, words):  # -> int
    wordsBits = list(map(toBits, words))
    lengths = list(map(len, words))
    return max([lengths[i] * lengths[j]
                for i in range(len(words))
                for j in range(i + 1, len(words))
                if not wordsBits[i] & wordsBits[j]] or [0])  # 位运算发挥优势的地方 O(1)完成集合的交


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxProduct(*args), end='\n-----\n')


  test(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
  test(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
  test(["a", "aa", "aaa", "aaaa"])
else:
  print = lambda *args, **kwargs: None
