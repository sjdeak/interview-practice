"""
ID: sjdeak1
LANG: PYTHON3
TASK: barn1
"""
import sys

sys.stdin = open("barn1.in")
sys.stdout = open("barn1.out", 'w')

if __name__ == '__main__':
  M, S, C = list(map(int, input().split()))
  cows = sorted([int(input()) for i in range(C)])
  gaps = list(filter(bool, [cows[i] - cows[i - 1] - 1 for i in range(1, C)]))

  # debug('empty_ranges:', gaps)

  originalBoardLength = max(cows) - min(cows) + 1

  ans = originalBoardLength - sum(sorted(gaps, reverse=True)[:(M - 1)] or [0])
  print(ans)
