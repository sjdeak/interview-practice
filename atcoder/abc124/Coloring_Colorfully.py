S = list(map(int, input()))
length = len(S)

dp = {}

for i in range(length):
  for j in range(2):
    if i == 0:
      dp[(i, j)] = 0 if S[0] == j else 1
      continue

    # print('i,j:', i, j)
    inverse = 0 if S[i] == 1 else 1

    if S[i] == j:  # 最后 S[i] 不动
      dp[(i, j)] = dp[(i - 1, inverse)]
    else:  # 最后 S[i] 变成inverse
      dp[(i, j)] = dp[(i - 1, S[i])] + 1

# print('dp', dp)
print(min(dp[(length - 1, 0)], dp[(length - 1, 1)]))
