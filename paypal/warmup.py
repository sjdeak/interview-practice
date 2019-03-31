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

for line in sys.stdin:
  N, M = map(int, line.split())

  students = list(range(1, N + 1))
  st = 0
  target = None
  for i in range(1, N):
    target = (st + M ** i - 1) % (len(students))
    newVal = students[(target + 1) % (len(students))]
    students.pop(target)
    # print('students', students)
    # 确定新的开始点
    st = students.index(newVal)

  print(students[0])
