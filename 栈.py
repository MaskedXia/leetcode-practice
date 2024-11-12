#84. 柱状图中最大的矩形
def largestRectangleArea(heights) -> int:
    # 哨兵单调栈
    res = 0
    stack = []
    heights = [0] + heights + [0]
    stack.append(0)
    lens = len(heights)
    for i in range(1, lens):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            res = max(res, h * w)
        stack.append(i)
    return res
print(largestRectangleArea([2,1,5,6,2,3]))

#85.最大矩形：给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积
def maximalRectangle(matrix):
    def ans84(heights):
        # 哨兵单调栈
        res = 0
        stack = []
        heights = [0] + heights + [0]
        stack.append(0)
        lens = len(heights)
        for i in range(1, lens):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

    row = len(matrix)
    if row == 0:
        return 0
    col = len(matrix[0])
    height = [0] * col
    max_area = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0
        cur = ans84(height)
        max_area = max(max_area, cur)
    return max_area

