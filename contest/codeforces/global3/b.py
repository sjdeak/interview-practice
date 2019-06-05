N, M, Ta, Tb, K = list(map(int, input().split()))
arriveAts = list(map(lambda s: (int(s) + Ta, 'arrive'), input().split()))
flights = list(map(lambda s: (int(s), 'go'), input().split()))

timeline = sorted(arriveAts + flights)
KLeft = K
arriveAt = None
ans = None
for t in timeline:
  now, type = t
  if type == 'arrive':
    arriveAt = now
  elif type == 'go':
    if arriveAt is not None and KLeft:
      # 干涉此航班
      KLeft -= 1
    else:
      ans = now
      break

print(-1 if ans is None else ans + Tb)
