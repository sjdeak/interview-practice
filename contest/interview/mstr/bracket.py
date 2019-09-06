from functools import lru_cache


# 长度为n的任何一个合法括号串 都可以从n=0开始逐个扩展得到
# 这是由括号串的定义得到的

@lru_cache(None)
def dp(n):
  if n % 2:
    return []

  if n == 0:
    return ['']

  pre = dp(n - 2)
  res = list(map(lambda s: s + '()', pre))
  res += list(map(lambda s: '()' + s, pre))
  res += list(map(lambda s: '(' + s + ')', pre))

  return list(set(res))


print('dp(8):', dp(8))
