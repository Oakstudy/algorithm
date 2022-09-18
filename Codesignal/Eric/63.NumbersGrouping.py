def solution(a):
    return len(set([(x-1) // 10000 for x in a])) + len(a)

print(solution([20000, 239, 10001, 999999, 10000, 20566, 29999])) # 11