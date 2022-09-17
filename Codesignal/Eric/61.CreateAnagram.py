def solution(s, t):
    for x in s:
        if x in t and (t.find(x) != -1):
            index = t.find(x)
            t = t[:index] + t[index+1:]
    return len(t)


def solution(s, t):
    s = list(s)
    for i in t:
        if i in s:
            s.remove(i)
    return len(s)

def solution(s, t):
    return sum([s.count(i) - t.count(i) for i in set(s) if s.count(i) - t.count(i) > 0])

print(solution("AABAA", "BBAAA")) # 1
print(solution("OVGHK", "RPGUC")) # 4
