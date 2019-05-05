# https://leetcode.com/contest/weekly-contest-135/problems/binary-search-tree-to-greater-sum-tree/
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


def getTreeNodeSum(node):
  if not node:
    return 0
  return node.val + getTreeNodeSum(node.left) + getTreeNodeSum(node.right)


# 递归修改树上节点 node.val → greaterSum
def dfs(node, type, parNode):
  if not node:
    return

  node.originalVal = node.val

  if type == 'right':
    node.val = parNode.val - parNode.originalVal - getTreeNodeSum(node.left)
  else:
    node.val = node.val + getTreeNodeSum(node.right) + parNode.val

  dfs(node.left, 'left', node)
  dfs(node.right, 'right', node)


class Solution:
  def bstToGst(self, root):  # -> TreeNode
    dfs(root, 'left', TreeNode(0))
    return root


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().bstToGst(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
