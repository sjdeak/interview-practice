input()
S = input()
length = len(S)

dp = {}

for i in range(length):
  for ch in ['#', '.']:
    base = 1 if S[i] != ch else 0

    if i == 0:
      dp[(i, ch)] = base
      continue
    if ch == '#':
      dp[(i, ch)] = min(base + dp[(i - 1, '#')], base + dp[(i - 1, '.')])
    else:
      dp[(i, ch)] = base + dp[(i - 1, '.')]

# print('dp', dp)
print(min(dp[(length - 1, '#')], dp[(length - 1, '.')]))
