def solution(n):
    el = {}
    while True:
        added = sum([int(x) for x in str(n)])
        el[added] = el[added] + 1 if el.get(added) else 1
        n -= added 
        if n == 0:
            break
        
    max_values = max(el.values())
    return sorted([k for k, v in el.items() if v == max_values])[-1]

print(solution(88)) # 9
print(solution(8)) # 8