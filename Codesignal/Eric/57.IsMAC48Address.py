def solution(inputString):
    sep = inputString.split('-')
    if len(sep) != 6:
        return False
    for x in sep:
        if len(x) != 2:
            return False
        if  not ((ord('0') <= ord(x[0]) <= ord('9') or ord('A') <= ord(x[0]) <= ord('F')) and
                 (ord('0') <= ord(x[1]) <= ord('9') or ord('A') <= ord(x[1]) <= ord('F')) ):
            return False
    return 


def solution(inputString):
    if len(inputString) != 17: return False
    for i in range(len(inputString)):
        if i % 3 == 2:
            if inputString[i] != '-': return False
        else:
            if inputString[i] not in '1234567890ABCDEF': return False
    return True
        

print(solution("00-1B-63-84-45-E6")) # true
print(solution("Z1-1B-63-84-45-E6")) # false
print(solution("not a MAC-48 address")) # false
print(solution("12-34-56-78-9A-")) # false
