# coding=utf-8
def solve_small(F, L):
  res = 0
  for i in range(F, L + 1):
    if '9' not in str(i) and i % 9:
      res += 1
  return res


def solve(F, L):
  return count(L) - count(F) + 1  # +1是因为F也被减掉了


# 计算[1,N]内的所有解
def count(N):
  res = 0
  L = len(str(N))
  # 从左往右遍历每一位
  for i, v in enumerate(str(N)):
    if i < L - 1:
      res += int(v) * (9 ** (L - 2 - i)) * 8
    else:
      for i in range(N - N % 10, N + 1):
        if i % 9 > 0:
          res += 1
      # res += N % 10 + (N % 9 > N % 10)
  return res
