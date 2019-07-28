import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy
sys.setrecursionlimit(1000000)
class CustomException(Exception): pass

if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, G, M = list(map(int, input().split()))
    Guests = []
    for i in range(G):
      H, Direction = input().split()
      Guests.append(namedtuple('Guest', ['id', 'st', 'direction'])(i, int(H) - 1, Direction))

    consulateRecords = defaultdict(list)
    # M %= N

    for guest in Guests:
      for t in range(M + 1):
        if guest.direction == 'C':
          consulateRecords[(guest.st + t) % N].append((t, guest.id))
        else:
          consulateRecords[(guest.st - t + N) % N].append((t, guest.id))

    debug('consulateRecords:', consulateRecords)

    counter = {i: 0 for i in range(G)}
    for consulateId in consulateRecords:
      consulate = consulateRecords[consulateId]
      consulate.sort(reverse=True)
      if consulate:
        for record in consulate:
          time, guestId = record
          if time == consulate[0][0]:
            counter[guestId] += 1

    debug('counter:', counter)

    print('Case #{}:'.format(caseIndex + 1), *counter.values())
