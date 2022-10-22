# def solution(s):
#     for i in range(len(s)-1):
#         if ord(s[i]) >= ord(s[i+1]):
#             return False
#     return True


# def solution(s):
#     return "".join(sorted(s)) == s and len(set(s)) == len(s)

def solution(s):
    return all([s[i] < s[i+1] for i in range(len(s)-1)])

print(solution("effg")) # false