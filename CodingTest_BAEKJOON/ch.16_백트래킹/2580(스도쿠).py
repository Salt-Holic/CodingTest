# import sys
#
# graphs = []
# blank = []
#
#
# def row_check(x, num):
#     for i in range(9):
#         if graphs[x][i] == num:
#             return False
#     return True
#
#
# def col_check(y, num):
#     for i in range(9):
#         if graphs[i][y] == num:
#             return False
#     return True
#
#
# def rect_check(x, y, num):
#     row = x // 3
#     col = y // 3
#     for i in range(row * 3, row * 3 + 1):
#         for j in range(col * 3, col * 3 + 1):
#             if graphs[i][j] == num:
#                 return False
#     return True
#
#
# def dfs(idx):
#     if idx == len(blank):
#         for i in range(9):
#             print(*graphs[i])
#         return
#
#     for i in range(1, 10):
#         x, y = blank[idx]
#
#         if row_check(x, i) and col_check(y, i) and rect_check(x, y, i):
#             graphs[x][y] = i
#             dfs(idx + 1)
#             graphs[x][y] = 0  # 재귀 내 정답이 없을 경우 0으로 초기화
#
#
# for i in range(9):
#     graphs.append(list(map(int, sys.stdin.readline().split())))
#
# for i in range(9):
#     for j in range(9):
#         if graphs[i][j] == 0:
#             blank.append((i, j))
#
# dfs(0)


import sys
graph = []
blank = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))


def dfs(idx):
    if idx == len(blank):
        return True
    x, y = blank[idx]

    flag = False
    for n in range(1, 10):
        if checkRow(x, y, n) and checkCol(x, y, n) and checkBox(x, y, n):
            flag = True
            graph[x][y] = n
            if not dfs(idx+1):
                graph[x][y] = 0
                flag = False

    return True if flag else False


def checkRow(x, y, n):
    for i in range(9):
        if i != y and graph[x][i] == n:
            return False
    return True


def checkCol(x, y, n):
    for i in range(9):
        if x != i and graph[i][y] == n:
            return False
    return True


def checkBox(x, y, n):
    a = 3 * (x//3)
    b = 3 * (y//3)
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if (i, j) != (x, y) and graph[i][j] == n:
                return False
    return True


dfs(0)
for i in range(9):
    for j in range(9):
        print(graph[i][j], end=' ')
    print()

