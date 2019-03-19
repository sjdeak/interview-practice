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


def postorderTraversal(node, func):
  if not node:
    return
  postorderTraversal(node.left, func)
  postorderTraversal(node.right, func)
  func(node)

class Solution:
  def postorderTraversal(self, root):
    res = []
    postorderTraversal(root, lambda nd: res.append(nd.val))
    return res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().postorderTraversal(*args), end='\n-----\n')

  test(array2TreeNode([1,None,2,3]))

