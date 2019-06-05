from operator import itemgetter

N = int(input())
edges = []
for _ in range(N):
  v, u = map(int, input().split())
  edges.append([u, v])
edges.sort(key=itemgetter(1))

dp = {}

# dp[i] 以区间i结尾的重叠区间的重叠数
for i in range(len(edges)):
  if i == 0:
    dp[i] = 1
    continue
  choices = [dp[i - 1]]
  iu, iv = edges[i]
  preU, preV = edges[i]
  if preV >= iu:
    choices.append(dp[i - 1] + 1)
  dp[i] = max(choices)

print('dp', dp)
print(max([dp[i] for i in range(len(edges))]))
