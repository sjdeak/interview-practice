def dfs(now, step):
  print('now, step, X', now, step, X)
  if step > X: return

  currentAt = now[-1]

  if now not in ignoredups:
    ignoredups.add(now)
  else:
    return

  if currentAt == P and 0 < step:
    ans.add(now)

  for n in range(1, N + 1):
    if n == currentAt: continue
    if (currentAt % n == 0) or (n % currentAt == 0):
      dfs(tuple(list(now) + [n]), step + 1)


N = input1
P = input2
X = input3
ans = set()
ignoredups = set()
dfs(tuple([P]), 0)
print('ans', ans)
return len(ans)
