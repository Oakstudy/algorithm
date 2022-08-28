def solution(inputString):
    for i in range(len(inputString)//2):
        if inputString[i].lower() != inputString[-1-i].lower():
            return False
    return True

def solution(s):
    return s.lower() == s[::-1].lower()

print(solution("AaBaa")) # true