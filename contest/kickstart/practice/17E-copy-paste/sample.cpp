for (int i = 0; i < len; i++) {
  dp[i + 1][0][0] = Math.min(dp[i + 1][0][0], dp[i][0][0] + 1); // #1
  for (int j = 0; j < i; j++) {
    for (int k = j + 1; k <= i; k++) { // 枚举剪贴板
      dp[i + 1][j][k] = Math.min(dp[i + 1][j][k], dp[i][j][k] + 1); // #2
      if (input.str.substring(i).startsWith(input.str.substring(j, k))) { // #3
        dp[i + k - j][j][k] = Math.min(dp[i + k - j][j][k], dp[i][j][k] + 1); // #4
        dp[i + k - j][j][k] = Math.min(dp[i + k - j][j][k], dp[i][0][0] + 2); // #5 先复制 [j,k)，再粘贴
        dp[i + k - j][0][0] = Math.min(dp[i + k - j][0][0], dp[i][j][k] + 1); // #6
        dp[i + k - j][0][0] = Math.min(dp[i + k - j][0][0], dp[i][0][0] + 2); // #7
      }
    }
  }
}

/*
#1: 直接输入下一个字母
#2: 直接输入下一个字母
#3: 判断此时粘贴是否合法（未输入的部分以剪贴板中的内容为前缀）
#4: 粘贴剪贴板中的内容
#5: 先复制 [j,k)，再粘贴（与之前剪贴板内容无关，故用当前 i 最优解 dp[i][0][0] 加即可）
#6, #7 与 #4, #5 同理
*/