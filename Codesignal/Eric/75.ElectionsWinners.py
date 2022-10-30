def solution(votes, k):
    result = 0
    s = sorted(votes)
    for i, v in enumerate(s):
        if (v + k) > s[-1]:
            result = len(votes) - i
            break
    if result == 0 and s[-1] != s[-2]:
        return 1
    return result

def solution2(votes, k):
    m = max(votes)
    if k == 0:
        return 1 if len([x for x in votes if x==m]) == 1 else 0
    return len([x for x in votes if x+k > m])

def solution3(votes, k):
    m = max(votes)
    return sum(v + k > m for v in votes) if k > 0 else 1 if votes.count(m) == 1 else 0

print(solution([2, 3, 5, 2], 3)) # 2
print(solution([1, 3, 3, 1, 1], 0)) # 0
print(solution([5, 1, 3, 4, 1], 0)) # 1
print(solution([1, 1, 1, 1], 1)) # 4