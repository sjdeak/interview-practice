import sys


def guess(n):
  print(n)
  sys.stdout.flush()  # 交互题 print 后 input 前需要 flush
  s = input()
  if s == 'CORRECT':
    return 0
  elif s == "TOO_SMALL":
    return 1
  else:
    return -1


# 从[a,b]里猜目标数字
def solve(a, b):
  left, right = a, b
  while left <= right:
    mid = left + (right - left) // 2

    resp = guess(mid)
    if resp == 0:
      return mid
    elif resp == 1:
      left = mid + 1
    else:
      right = mid - 1


if __name__ == '__main__':
  T = int(input())
  for _ in range(T):
    a, b = map(int, input().split())
    _ = int(input())
    solve(a + 1, b)
