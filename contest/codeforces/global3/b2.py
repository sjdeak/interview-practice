import os
from bisect import bisect_left
from math import inf

if os.getenv('SJDEAK'):
  debug = print
else:
  debug = lambda *args, **kwargs: None

N, M, Ta, Tb, K = list(map(int, input().split()))
arriveAts = list(map(lambda s: int(s) + Ta, input().split()))
flights = list(map(int, input().split()))

ansI = -inf
for i, arriveAt in enumerate(arriveAts[:K + 1]):  # i: 干涉了 到达 几次
  nearestFlightIndex = bisect_left(flights, arriveAt)
  ansI = max(ansI, nearestFlightIndex + (K - i))
  debug('i, arriveAt, nearestFlightIndex, ansI:', i, arriveAt, nearestFlightIndex, ansI)

print(-1 if K >= N or ansI == -inf or ansI > M - 1 else flights[ansI] + Tb)
