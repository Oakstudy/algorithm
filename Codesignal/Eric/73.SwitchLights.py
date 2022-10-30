def solution(a):
    result = []
    for i in range(len(a)):
        acc = 0
        for j in range(i, len(a)):
            acc += a[j]
        result.append(a[i] if acc % 2 == 0 else abs(a[i]-1))
    return result
            
def solution2(a):
    return [(x + sum(a[i:]))%2 for i,x in enumerate(a)]

def solution3(a):
    flips = 0
    for i in range(len(a)-1,-1,-1):
        if a[i]==1:
            flips +=1
        a[i] = (a[i]+flips)%2
    return a

def solution4(a):
    for i in range(len(a)):
        if a[i]:
            for j in range(i+1):
                a[j]=1-a[j]
    return a

print(solution2([1, 1, 1, 1, 1])) # [0, 1, 0, 1, 0]