def solution(f1, f2):
    return (f1.lower() < f2.lower()) != (f1 < f2)

    
print(solution("aa", "AAB"))
print(solution("A", "z"))