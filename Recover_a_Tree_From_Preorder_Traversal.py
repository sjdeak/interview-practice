# https://leetcode.com/contest/weekly-contest-132/problems/recover-a-tree-from-preorder-traversal/
# 1ac 😀
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
  # 处理node的左右节点
  def dfs(self, node, depth):
    if not self.S.startswith('-' * depth):
      return

    self.S = self.S.replace('-' * depth, '', 1)
    leftVal = self.getVal()
    node.left = TreeNode(leftVal)
    self.dfs(node.left, depth + 1)

    if not self.S.startswith('-' * depth):
      return

    self.S = self.S.replace('-' * depth, '', 1)
    rightVal = self.getVal()
    node.right = TreeNode(rightVal)
    self.dfs(node.right, depth + 1)

  def getVal(self):
    matches = re.match(r'^(\d+)', self.S)

    if matches:
      value = int(matches.group(1))
      self.S = self.S.replace(str(value), '', 1)
      print('getVal:', value)
      return value
    else:
      return -1

  def recoverFromPreorder(self, S):  # -> TreeNode
    self.S = S
    root = None
    val = self.getVal()
    if val != -1:
      root = TreeNode(val)
      self.dfs(root, 1)

    return root


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().recoverFromPreorder(*args), end='\n-----\n')


  test("1-2--3--4-5--6--7")
  # test("1-2--3---4-5--6---7")
  # test("1-401--349---90--88")
else:
  print = lambda *args, **kwargs: None
