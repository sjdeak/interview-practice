def move(a, b, step):
  a.val -= 1
  b.val += 1
  dfs(nodes, step + 1)
  a.val += 1
  b.val -= 1


def refreshGlobals():
  global ignoredups, ans
  ignoredups = {}
  ans = 10 ** 20


dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def dfs(nodes, step):
  # 排除非法移动

  # 判重
  tcoins = tuple(coins)
  if tcoins in ignoredups and ignoredups[tcoins] <= step:
    return
  else:
    ignoredups[tcoins] = step

  # 最优性剪枝
  if step > ans:
    return

  # 判断是否到达终点
  if all([c == 1 for c in coins]):
    ans = min(step, ans)
    return

  # 移动
  for nd in nodes:
    pass
