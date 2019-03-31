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


def linkList2Array(node):
  res = []
  while node:
    res.append(node.val)
    node = node.next
  return res


# TLE: Next Greater Node In Linked List
class Solution:
  def nextLargerNodes(self, head):  # -> List[int]
    arr = linkList2Array(head)
    length = len(arr)
    ans = [0] * length
    for i, n in enumerate(arr):
      for j in range(i + 1, length):
        if arr[j] > n:
          ans[i] = arr[j]
          break
    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().nextLargerNodes(*args), end='\n-----\n')

  # test([2,1,5])
  # test([2,7,4,3,5])
  # test([1,7,5,1,9,2,5,1])
