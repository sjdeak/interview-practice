a, b, c = list(map(int, input().split()))
ans = 2 * c + 2 * min(a, b) + int(bool(max(a, b) - min(a, b)))
print(ans)
