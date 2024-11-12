#22.括号生成
def generateParenthesis(n):
    ans = []
    def backtrack(S, left, right):
        if len(S) == 2 * n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S, left + 1, right)
            # 可以缩写backtrack(S+’(’, left+1, right)，就不用pop了
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S, left, right + 1)
            S.pop()
    backtrack([], 0, 0)
    return ans
#print(generateParenthesis(3))

#37.解数独
# •	给定的数独序列只包含数字 1-9 和字符 '.' 。cur
# •	你可以假设给定的数独只有唯一解。
# •	给定数独永远是 9x9 形式的
def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
    col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
    block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
    empty = []  # 收集需填数位置
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':  # 更新可用数字
                val = int(board[i][j])
                row[i].remove(val)
                col[j].remove(val)
                block[(i // 3) * 3 + j // 3].remove(val)
            else:
                empty.append((i, j))
    def backtrack(iter=0):
        if iter == len(empty):  # 处理完empty代表找到了答案
            return True
        i, j = empty[iter]
        b = (i // 3) * 3 + j // 3
        for val in row[i] & col[j] & block[b]:  # 求集合的交集&
            row[i].remove(val)
            col[j].remove(val)
            block[b].remove(val)
            board[i][j] = str(val)
            if backtrack(iter + 1):
                return True
            row[i].add(val)  # 回溯
            col[j].add(val)
            block[b].add(val)
        return False
    backtrack()

#40.组合总和:给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
def combinationSum2(candidates, target):
    lens = len(candidates)
    cur = []
    res = []
    if lens == 0:
        return []
    candidates.sort()
    def get(cur, res, begin, target):
        if target == 0:
            res.append(cur[:])
        for index in range(begin, lens):
            remain = target - candidates[index]
            if remain < 0:
                break
            if index > begin and candidates[index] == candidates[index-1]:  # 防止重复
                continue
            cur.append(candidates[index])
            # print(cur)
            get(cur, res, index + 1, remain)
            cur.pop()
    get(cur, res, 0, target)
    return res
#print(combinationSum2([10,2,3,7,6,1,5], 8))

#47.全排列:给定一个可包含重复数字的序列，返回所有不重复的全排列。
def permuteUnique(nums):
    lens = len(nums)
    if lens == 0:
        return []
    depth = 0  # 表示当前深度
    used = [False for i in range(lens)]  # 表示当前位置是否用过
    res = []
    path = []  # 当前的路径
    nums.sort()
    def dsf(depth, path, used, res):
        if depth == lens:
            res.append(path[:])
            return
        for i in range(lens):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i-1]:  #
                    continue
                used[i] = True
                path.append(nums[i])
                dsf(depth + 1, path, used, res)
                used[i] = False
                path.pop()
    dsf(depth, path, used, res)
    return res
print(permuteUnique([1,1,2]))

#79.单词搜索:给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#单词必须按照字母顺序，通过相邻的单元格内的字母构成，
# 其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def backtrack(i, j, mark, board, word):
    if len(word) == 0:
        return True
    for direct in directs:
        cur_i = i + direct[0]
        cur_j = j + direct[1]
        if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
            # 如果是已经使用过的元素，忽略
            if mark[cur_i][cur_j] == 1:
                continue
            # 将该元素标记为已使用
            mark[cur_i][cur_j] = 1
            if backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                return True
            else:
                # 回溯
                mark[cur_i][cur_j] = 0
    return False
def exist(board, word):
    m = len(board)
    if m == 0:
        return False
    n = len(board[0])
    mark = [[0] * n for _ in range(m)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                # 将该元素标记为已使用
                mark[i][j] = 1
                if backtrack(i, j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[i][j] = 0
    return False

#93.复原IP地址:给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
def restoreIpAddresses(s):
    res = []
    n = len(s)
    def backtrack(i, tmp, flag):
        if i == n and flag == 0:
            res.append(tmp[:-1])
            return
        if flag < 0:
            return
        for j in range(i, i + 3):
            if j < n:
                if i == j and s[j] == "0":
                    backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                    break  # 0开头是0只能单独占位
                if 0 < int(s[i:j + 1]) <= 255:
                    backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)
    backtrack(0, "", 4)
    return res

#130.被围绕的区域:给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
def solve(board):
    if not board or not board[0]:
        return
    row = len(board)
    col = len(board[0])
    def dfs(i, j):
        board[i][j] = 'B'
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            cur_i = i + x
            cur_j = j + y
            if 1 <= cur_i <= row - 2 and 1 <= cur_j <= col - 2 and board[cur_i][cur_j] == 'O':
                dfs(cur_i, cur_j)
    for i in range(row):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][col - 1] == 'O':
            dfs(i, col - 1)
    for j in range(col):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[row - 1][j] == 'O':
            dfs(row - 1, j)
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'B':
                board[i][j] = 'O'

#200.岛屿数量:给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
def numIslands(grid):
    def dfs(r, c):
        grid[r][c] = '0'
        for x, y in {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                dfs(x, y)

    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])
    res = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == '1':
                res += 1
                dfs(i, j)
    return res

#131.分割回文串:给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
def partition(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for r in range(n):
        for l in range(r + 1):
            if s[l] == s[r] and (r - l < 2 or dp[l + 1][r - 1]):
                dp[l][r] = True
    res = []

    def helper(i, tmp):
        if i == n:
            res.append(tmp)
        for j in range(i, n):
            if dp[i][j]:
                helper(j + 1, tmp + [s[i:j + 1]])

    helper(0, [])
    return res


