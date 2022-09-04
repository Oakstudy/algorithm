def solution2(a, b):
    first = {x: a.count(x) for x in set(a)}
    second = {x: b.count(x) for x in set(b)}
    result = len(b)
    isUpdated = False
    for key, value in first.items():
        if second.get(key):
            isUpdated = True
            result = min(result, second.get(key) // value)
        else:
            return 0
    return result if isUpdated else 0


def solution(a,b):
    return min(b.count(x)//a.count(x) for x in set(a))



print(solution('abc','abccba')) # 2
print(solution('ab','abcbcb')) # 1
