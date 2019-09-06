def MaxLIS_Lengths(numToys, tagList):
  # WRITE YOUR COE HERE
  # O(n^2) solution
  dp = {}
  for i in xrange(numToys - 1, -1, -1):
    for j in xrange(i, numToys):
      if i == j:
        dp[i, j] = True
        continue

      if tagList[i] < tagList[i + 1] and tagList[j - 1] > tagList[j]:
        dp[i, j] = dp[i + 1, j - 1]
      else:
        dp[i, j] = False

  print
  dp

  ans = 0
  for k in dp:
    if dp[k] == True:
      i, j = k
      ans = max(ans, j - i + 1)

  return ans
