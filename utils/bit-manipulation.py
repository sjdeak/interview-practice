# 判断两个字符串是否有相同的字符
# 时间复杂度 O(len(s1)+len(s2)) 空间复杂度 O(1)
# 频繁调用时可以提前打表(把所有字符串都先转成二进制表示)加速
def hasSameCh(s1, s2):
  def toBits(s):
    res = 0
    for ch in s:
      res |= 1 << (ord(ch) - ord('a'))
    return res

  ans = toBits(s1) & toBits(s2)
  # print('s1, s2, ans:', s1, s2, ans)
  return ans
