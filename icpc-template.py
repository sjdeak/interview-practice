import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter
from operator import itemgetter
from math import sqrt


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./icpc-data/in.txt'))
  # sys.stdout = open(os.path.expanduser('~/data/out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

if __name__ == '__main__':
  pass
