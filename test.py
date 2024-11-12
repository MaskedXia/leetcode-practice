def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    row = len(rooms)
    col = len(rooms[0])
    INF = 2147483647
    if row == 0:
        return
    queue = []
    for r in range(row):
        for c in range(col):
            if rooms[r][c] == 0:
                queue.append((r, c, 0))
    while queue:
        i, j, step = queue.pop(0)
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ci = di + i
            cj = dj + j
            if 0 <= ci < row and 0 <= cj < col and rooms[ci][cj] == INF:
                rooms[ci][cj] = step + 1
                queue.append((ci, cj, step + 1))