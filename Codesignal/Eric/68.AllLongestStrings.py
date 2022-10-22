def solution(input):
    length = len(sorted(input, key=len)[-1])
    return [x for x in input if len(x) == length]
    
    
print(solution(["a", 
 "abc", 
 "cbd", 
 "zzzzzz", 
 "a", 
 "abcdef", 
 "asasa", 
 "aaaaaa"]))

