#5.最长回文子串：给定一个字符串，找到s的最长回文子串
def longestPalindrome(s):
    size = len(s)
    if size <= 1:
        return s
    # 二维 dp 问题，动态规划问题
    # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
    dp = [[False for _ in range(size)] for _ in range(size)]
    longest_l = 1
    res = s[0]  # 置初始状态，重点（初始态）
    # 因为只有 1 个字符的情况在最开始做了判断
    # 左边界一定要比右边界小，因此右边界从 1 开始
    for r in range(1, size):
        for l in range(r):
            # 状态转移方程：如果头尾字符相等并且中间也是回文
            # 还要考虑长度很短的情况下
            if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                dp[l][r] = True
                cur_len = r - l + 1
                if cur_len > longest_l:
                    longest_l = cur_len
                    res = s[l:r + 1]
    return res

#72.编辑距离：给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
def minDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    # 第一行
    for j in range(1, n2 + 1):
        dp[0][j] = dp[0][j - 1] + 1
    # 第一列
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i - 1][0] + 1
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    return dp[-1][-1]



