import re

def solution(ml, text):
    result = 0
    arr = text.split(" ")
    for x in arr:
        match = re.findall(r'[a-zA-Z]+', x)
        if match and len(match[0]) <= ml:
            result += 1
    return result


# split 할때 여러개의 delimiter를 동시에 사용할 수 있다.        
def solution2(maxLength, text):
    return sum(1 for i in re.split("[] ;',:?!]",text) if maxLength >= len(i) and i)


def test(maxLength, text):
    return [ i for i in re.split("[] ;',:?!]",text)]

print(solution2(4, "The Fox asked the stork, 'How is the soup?'")) # 7
print(solution2(1, "...")) # 0
print(solution2(3, "This play was good for us.")) # 3