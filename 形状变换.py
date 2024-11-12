#6.Z字形变换：将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
def convert(s, numRows):
    if numRows < 2: return s
    res = ["" for _ in range(numRows)]
    i, flag = 0, -1  # 正常flag往下逐渐加一，对应索引加一；反转flag往上减一，对应索引减一
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return "".join(res)

#48.旋转图像：给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

            # reverse each row
    for i in range(n):
        matrix[i].reverse()
    # matrix[:] = zip(*matrix[::-1])#反转，转置

#54.螺旋矩阵：给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，
# 返回矩阵中的所有元素。
def spiralOrder(matrix):
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in range(R)]  # 表示是否被访问过了
    ans = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]  # 右下左上
    r = c = di = 0
    for _ in range(R * C):
        ans.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return ans


