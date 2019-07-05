# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aae
import os
import sys
from copy import deepcopy


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in2.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    R, C, K = map(int, input().split())
    Grid = [list(map(int, input().split())) for r in range(R)]
    # debug('Grid:', Grid)

    # minVal[i][j]表示从点(i,j)开始,向右延伸的长度是recLen的区间内的最小值
    minVal, maxVal = deepcopy(Grid), deepcopy(Grid)

    ans = 0
    for recLen in range(1, C + 1):
      for c in range(C - recLen + 1):  # 矩形左上角横坐标
        continuousCnt = 0
        for r in range(R):
          # 矩形左上角              矩形右上角
          minVal[r][c] = min(minVal[r][c], minVal[r][c + recLen - 1])
          maxVal[r][c] = max(maxVal[r][c], maxVal[r][c + recLen - 1])

          if maxVal[r][c] - minVal[r][c] <= K:
            continuousCnt += 1
            ans = max(ans, continuousCnt * recLen)
          else:
            continuousCnt = 0

    print('Case #{}: {}'.format(caseIndex + 1, ans))
