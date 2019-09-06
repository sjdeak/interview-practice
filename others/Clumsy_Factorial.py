import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter


class Solution:
  def clumsy(self, N: int) -> int:
    pass


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  def test(*args):
    print('输入数据: ', *args,
          '\n结果: ', Solution().clumsy(*args), end='\n-----\n')

  test(4)
  test(10)
