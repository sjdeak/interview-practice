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
  # sys.stdin = open(os.path.expanduser('./in-standard.txt'))
  # sys.stdin = open(os.path.expanduser('./in-anticlockwise.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


def getDistOnLoop(st, ed, circleSize, direction):
  """
  >>> getDistOnLoop(1, 4, 5, 'A')
  2
  >>> getDistOnLoop(4, 0, 5, 'C')
  1
  """
  if direction == 'C':
    if st > ed:
      return ed + circleSize - st
    else:
      return ed - st
  else:
    if st < ed:
      return st + circleSize - ed
    else:  # st >= ed 正常情况
      return st - ed


def getLastVisitGroupId(stopAts, cid, circleSize, direction):
  """
  # >>> getLastVisitGroupId([4, 3], 0, 5, 'A')
  # 4
  >>> getLastVisitGroupId([4, 3], 3, 5, 'A')
  3
  """
  left, right = 0, len(stopAts) - 1
  getDist = lambda i: getDistOnLoop(cid, stopAts[i], circleSize, direction)
  # 找getDistOnLoop(i) >= 0的第一个
  while left < right:
    mid = left + (right - left) // 2
    if getDist(mid) < 0:
      left = mid + 1
    else:
      right = mid

  if getDist(left) >= 0:
    return stopAts[left]
  else:
    return -1


def calculateClockwiseRecords():
  res = defaultdict(list)  # consulateRecords {consulate: [guestId1, guestId2]最后经过的那些人}
  guestStopAt = {}
  group = defaultdict(list)  # {stopAt: [guestId1, guestId2]}
  for gId, gSt, _ in GuestsClockwise:
    stopAt = (gSt + M) % N
    guestStopAt[gId] = stopAt
    group[stopAt].append(gId)

  debug('group:', group)

  arr = sorted(group.keys())
  # 对于使馆cid，找到它记住的那个group (第一个>=cid的stopAt)
  # choices = [0, 3, 7]  cid = 3
  for cid in range(N):
    bsRes = bisect_left(arr, cid)
    visitAt = None
    if bsRes == len(arr):  # 找不到 >= cid 的数, arr里所有元素都 < cid
      if hasLoop:  # 多圈的情况
        groupId = arr[0]
        visitAt = (M + (cid - groupId)) - N  # M + 如果能再走几步就能走到 - 一圈
      else:
        groupId = -1
    else:
      groupId = arr[bsRes]
      visitAt = M - (groupId - cid)  # 这步比较直观

    if groupId != -1:
      res[cid] += list(map(lambda gId: namedtuple('Record', ['guestId', 'visitAt'])(gId, visitAt),
                           group[groupId]))
  return res


def calculateAntiClockwiseRecords():
  res = defaultdict(list)  # consulateRecords {consulate: [guestId1, guestId2]最后经过的那些人}
  guestStopAt = {}
  group = defaultdict(list)  # {stopAt: [guestId1, guestId2]}
  for gId, gSt, _ in GuestsAntiClockwise:
    delta = M % N
    stopAt = gSt - delta
    stopAt = stopAt + N if stopAt < 0 else stopAt

    guestStopAt[gId] = stopAt
    group[stopAt].append(gId)

  debug('group:', group)

  arr = sorted(group.keys(), reverse=True)  # ⭐ 注意是reverse了的
  # 对于使馆cid，找到它记住的那个group (第一个>=cid的stopAt)
  # choices = [0, 3, 7]  cid = 3
  for cid in range(N):
    groupId = getLastVisitGroupId(arr, cid, N, 'A')

    if groupId != -1:
      visitAt = M - getDistOnLoop(cid, groupId, N, 'A')
      if visitAt > 0:
        res[cid] += list(map(lambda gId: namedtuple('Record', ['guestId', 'visitAt'])(gId, visitAt),
                             group[groupId]))
  return res


if __name__ == '__main__':
  import doctest

  doctest.testmod()
  assert 0

  T = int(input())
  for caseIndex in range(T):
    N, G, M = list(map(int, input().split()))
    debug('N, M:', N, M)
    GuestsClockwise, GuestsAntiClockwise = [], []
    for i in range(G):
      H, Direction = input().split()
      guest = namedtuple('Guest', ['id', 'st', 'direction'])(i, int(H) - 1, Direction)
      if guest.direction == 'C':
        GuestsClockwise.append(guest)
      else:
        GuestsAntiClockwise.append(guest)

    GuestsClockwise.sort(key=itemgetter(1))  # 按出发点从小往大排
    GuestsAntiClockwise.sort(key=itemgetter(1))
    hasLoop = M > N

    debug('GuestsClockwise:', GuestsClockwise)

    # 构建consulateRecords
    # clockwiseConsulateRecords = calculateClockwiseRecords()
    # debug('clockwiseConsulateRecords:', clockwiseConsulateRecords)
    clockwiseConsulateRecords = defaultdict(list)
    antiClockwiseConsulateRecords = calculateAntiClockwiseRecords()
    debug('antiClockwiseConsulateRecords:', antiClockwiseConsulateRecords)
    # antiClockwiseConsulateRecords = {}

    # 把两个记录合起来
    consulateRecords = clockwiseConsulateRecords
    for k, v in antiClockwiseConsulateRecords.items():
      consulateRecords[k] += v
    debug('consulateRecords:', *consulateRecords.items(), sep='\n')

    assert 0

    counter = defaultdict(int)
    for cid in consulateRecords:
      records = consulateRecords[cid]
      records.sort(reverse=True)

      if records:
        for record in records:
          if record.visitAt == records[0].visitAt:
            counter[record.guestId] += 1

    debug('counter:', counter)

    print('Case #{}:'.format(caseIndex + 1), *counter.values())
