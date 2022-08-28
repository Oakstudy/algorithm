def solution(inputString):
    half = len(inputString)//2
    return inputString[:half] == inputString[half:]
    
print(solution("tandemtandem"))
print(solution("qqq"))
print(solution("2w2ww"))