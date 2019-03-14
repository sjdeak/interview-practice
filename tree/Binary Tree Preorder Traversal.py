#!/usr/local/bin/python3
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


class Solution:
    def __init__(self):
        self.data = []
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.data.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.data


if __name__ == '__main__' and ('SJDEAK' in os.environ):
    def test(*args):
        print('测试: ', *args,
              '\n结果: ', Solution().preorderTraversal(*args), end='\n-----\n')

