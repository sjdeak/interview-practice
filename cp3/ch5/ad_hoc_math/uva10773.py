import os, sys
from itertools import count, combinations
from collections import namedtuple, Counter
from operator import itemgetter
from math import sin, cos, sqrt


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('~/data/in.txt'))
  # sys.stdout = open(os.path.expanduser('~/data/out.txt'), 'w')

if __name__ == '__main__':
  T = int(input())
  for case in range(T):
    d, v, u = map(int, input().split())  # u: boat_speed, v: flow_speed
    if u <= v or not v:
      print("Case {}: can't determine".format(case + 1))
      continue
    fastest_time = d / u
    shortest_path_time = d / (u * sqrt(1 - (v / u) ** 2))
    print("Case {}: {:.3f}".format(case + 1, shortest_path_time - fastest_time))
