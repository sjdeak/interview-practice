# https://leetcode.com/contest/weekly-contest-132/problems/maximum-difference-between-node-and-ancestor/
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
  def getMinMax(self, node):
    minVal, maxVal = node.val, node.val

    print('node.val, ans:', node.val, self.ans)

    if node.left:
      minChildValLeft, maxChildValLeft = self.getMinMax(node.left)
      print('minChildValLeft, maxChildValLeft:', minChildValLeft, maxChildValLeft)

      self.ans = max(abs(node.val - minChildValLeft), abs(node.val - maxChildValLeft), self.ans)
      minVal, maxVal = min(minChildValLeft, minVal), max(maxChildValLeft, maxVal)
    if node.right:
      minChildValRight, maxChildValRight = self.getMinMax(node.right)
      print('minChildValRight, maxChildValRight:', minChildValRight, maxChildValRight)

      self.ans = max(abs(node.val - minChildValRight), abs(node.val - maxChildValRight), self.ans)
      minVal, maxVal = min(minChildValRight, minVal), max(maxChildValRight, maxVal)

    return minVal, maxVal

  def maxAncestorDiff(self, root):  # -> int
    self.ans = 0
    self.getMinMax(root)
    return self.ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxAncestorDiff(*args), end='\n-----\n')


  test(array2TreeNode('[8,3,10,1,6,null,14,null,null,4,7,13]'))
  # test()
else:
  print = lambda *args, **kwargs: None
