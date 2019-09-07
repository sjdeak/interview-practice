# Read only region start
class UserMainCode(object):
  @classmethod
  def points(cls, input1, input2):
    '''
    input1 : int
    input2 : int[]

    Expected return type : int
    '''

    def isPalindromic(s):
      return s == s[::-1]

    N = input1
    Seq = ''.join(map(str, input2))
    dp = {}

    for i in range(N - 1, -1, -1):
      for j in range(i, N):
        print('i,j', i, j)
        if isPalindromic(Seq[i:j + 1]):
          dp[(i, j)] = 1
          continue
        if j - i == 1:
          dp[(i, j)] = 1 if isPalindromic(Seq[i:j + 1]) else 2
          continue

        choices = []
        for k in range(i + 1, j):  # 中间切
          choices.append(dp[(i, k - 1)] + dp[(k + 1, j)] + 1)  # 2,2
          if isPalindromic(Seq[i:k] + Seq[k + 1:j + 1]):
            choices.append(2)

        choices.append(1 + dp[i + 1, j])  # 去头
        choices.append(dp[(i, j - 1)] + 1)  # 去尾
        dp[(i, j)] = min(choices)

    print('dp:', dp)
    return dp[(0, N - 1)]


"""
seq = map(str, input2).join('')
          dfs(seq, 0)

        def dfs(now, step):
          if not now:
            ans = min(ans, step)
            return

          if step > ans: return

          if now not in ignoredups:
            ignoredups[now] = step
          else:
            if step >= ignoredups[now]:
              return
            else:
              ignoredups[now] = step

        ans = 10 ** 20
        ignoredups = {}

"""
