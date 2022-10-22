from pprint import pprint

def solution(picture):
    result = []
    result.append('*' * (len(picture[0]) + 2))
    for row in picture:
        result.append('*' + row + '*')
    result.append('*' * (len(picture[0]) + 2))
    return result

def solution2(picture):
    stars = ['*' * (len(picture[0]) + 2)] 
    return stars + ['*' + row + '*' for row in picture] + stars

pprint(solution2(["abc", "ded"]))