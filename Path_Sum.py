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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isLeaf(root):
  return (not root.left) and (not root.right)


class Solution:
  def hasPathSum(self, root, sum: int) -> bool:
    if not root:
       return False
    if isLeaf(root):
      return sum == root.val
    resL = self.hasPathSum(root.left, sum-root.val)
    resR = self.hasPathSum(root.right, sum-root.val)
    return resL or resR


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().hasPathSum(*args), end='\n-----\n')

  test(array2TreeNode([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22)
