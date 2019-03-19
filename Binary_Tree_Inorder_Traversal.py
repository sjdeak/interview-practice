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



def inorderTraversal(node, func):
  if not node:
    return
  inorderTraversal(node.left, func)
  func(node)
  inorderTraversal(node.right, func)


class Solution:
  def inorderTraversal(self, root):
    res = []
    inorderTraversal(root, lambda nd: res.append(nd.val))
    return res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().inorderTraversal(*args), end='\n-----\n')

  test(array2TreeNode([1,None,2,3]))

