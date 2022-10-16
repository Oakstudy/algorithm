def solution(legs):
    result = []
    while legs >= 0:
        result.append(legs//2)
        legs -= 4
    return result[::-1]


print(solution(6)) # [4,2]