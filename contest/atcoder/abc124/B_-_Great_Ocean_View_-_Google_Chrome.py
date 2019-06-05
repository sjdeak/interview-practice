N = int(input())
H = list(map(int, input().split()))

cnt = 0
for i, n in enumerate(H):
  if all([H[j] <= n for j in range(i)]):
    cnt += 1

print(cnt)
