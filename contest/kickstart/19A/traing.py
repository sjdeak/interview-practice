from operator import itemgetter

# todo 大数据量需要线段树来做优化?

T = int(input())
for t in range(T):
  N, P = map(int, input().split())
  S = list(map(int, input().split()))
  S.sort()
  # print('S', S)

  costs = []
  for i in range(0, len(S) - P + 1):
    cost = (P - 1) * S[i + P - 1] - sum([S[j] for j in range(i, i + P - 1)])
    costs.append((i, cost))

  # print('costs', costs)

  # think 为什么非要写key= ?
  ansTuple = min(costs, key=itemgetter(1))
  ans = ansTuple[1]

  print("Case #{}: {}".format(t + 1, ans))
