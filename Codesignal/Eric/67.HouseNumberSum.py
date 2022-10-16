def solution2(input):
    result = 0
    for v in input:
        if v == 0:
            break
        result += v
    return result

def solution(input):
    return sum(input[:input.index(0)])
    

print(solution([5, 1, 2, 3, 0, 1, 5, 0, 2]))