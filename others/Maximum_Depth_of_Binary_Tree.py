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



class Solution:
  def maxDepth(self, root) -> int:
    if not root:
      return 0
    dl = self.maxDepth(root.left)
    dr = self.maxDepth(root.right)
    return max(dl, dr) + 1


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxDepth(*args), end='\n-----\n')

  test(array2TreeNode([3,9,20,None,None,15,7]))

