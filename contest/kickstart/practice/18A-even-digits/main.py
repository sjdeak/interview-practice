import os
import sys


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in-large.txt'))
  # sys.stdout = open(os.path.expanduser('./out-large.txt'), 'w')
  from icpc_util import dump_args
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func

isOdd = lambda d: int(d) % 2
toInt = lambda l: int(''.join(l))


@dump_args
def solveMinus(digits: [str]):
  if len(digits) == 1:
    return 1 if isOdd(digits[0]) else 0

  for i, digit in enumerate(digits):
    if isOdd(digit):
      if i != len(digits) - 1:
        return toInt(digits[i:]) - toInt([str(int(digit) - 1)] + ['8'] * (len(digits[i:]) - 1))
      else:
        return solveMinus(digit)
  else:
    return 0


def solvePlus(digits):
  if len(digits) == 1:
    return 1 if isOdd(digits[0]) else 0

  for i, digit in enumerate(digits):  # digit: 当前位的字符串
    if isOdd(digit):
      if digit != '9':
        return toInt([str(int(digit) + 1)] + ['0'] * (len(digits[i:]) - 1)) - toInt(digits[i:])
      else:
        if i == 0:
          up = ['1'] + ['0'] * len(digits)
        else:
          up = [str(int(digits[i - 1]) + 1)] + ['0'] * len(digits[i:])
        return solvePlus(up) + toInt(up) - toInt(digits[i:])
  else:
    return 0


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N = list(input())

    resPlus = solvePlus(N)
    resMinus = solveMinus(N)
    # debug('N, resPlus, resMinus:', N, resPlus, resMinus)
    ans = min(resPlus, resMinus)
    # ans = solvePlus(N)
    print(f'Case #{caseIndex + 1}: {ans}')
