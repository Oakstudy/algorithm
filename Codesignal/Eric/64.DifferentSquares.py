def solution(m):
    row = len(m)
    col = len(m[0])
    s_list = []
    for r in range(row-1):
        for c in range(col-1):
            square = [m[r][c], m[r+1][c], m[r+1][c+1], m[r][c+1]]
            if square not in s_list:
                s_list.append(square)
    return len(s_list)


print(solution([[1, 2, 1],
                [2, 2, 2],
                [2, 2, 2],
                [1, 2, 3],
                [2, 2, 1]]))