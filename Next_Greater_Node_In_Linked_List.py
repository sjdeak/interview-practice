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


def getNextLarger(i, arr, nextLargerIndexArr):
  now = i + 1
  while now != -1:
    if arr[now] > arr[i]:
      return now
    now = nextLargerIndexArr[now]
  return -1


class Solution:
  def nextLargerNodes(self, head):  # -> List[int]
    arr = linkList2Array(head)
    length = len(arr)
    if length == 1:
      return [0]

    nextLargerIndexArr = [0] * length  # 最后放最终结果 [next_larger(i), ...]

    nextLargerIndexArr[length - 1] = -1
    for i in range(length - 2, -1, -1):
      nextLargerIndexArr[i] = getNextLarger(i, arr, nextLargerIndexArr)
    # print('nextLargerIndexArr', nextLargerIndexArr)

    ans = [arr[index] if index != -1 else 0 for index in nextLargerIndexArr]
    # print('ans', ans)

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().nextLargerNodes(*args), end='\n-----\n')

  # test([2,1,5])
  # test([2,7,4,3,5])
  # test([1,7,5,1,9,2,5,1])
