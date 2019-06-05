import sys
from collections import Counter


def getUnmatches(s):
  left, right = 0, len(s) - 1
  res = []
  while left < right:
    if s[left] != s[right]:
      res.append(tuple(sorted([s[left], s[right]])))
    left, right = left + 1, right - 1
  return res


def condition1(s):
  unmatches = getUnmatches(s)
  # print('unmatches:', unmatches)
  if len(unmatches) != 2:
    return False
  um1, um2 = unmatches
  return um1 == um2


def condition2(s):
  centerCh = s[len(s) // 2]
  unmatches = getUnmatches(s)
  if len(unmatches) != 1:
    return False
  um = unmatches[0]
  return um[0] == centerCh or um[1] == centerCh


def canBePalindrome(s):
  # print('s, condition1(s), condition2(s):', s, condition1(s), condition2(s))

  if s == s[::-1] and len(s) > 1:
    return True

  if len(s) % 2:
    return condition1(s) or condition2(s)
  else:
    return condition1(s)


for line in sys.stdin:

  s = line.strip()
  if canBePalindrome(s):
    print('Yes')
  else:
    print('No')
