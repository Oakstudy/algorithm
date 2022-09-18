def solution(s):
    m_list = []
    n = 1
    while True:
        m = str(n*n)
        m_len = len(m)
        if len(s) == m_len:
            m_list.append(m)
        if m_len > len(s):
            break
        n = n + 1
    m_list = m_list[::-1]
    
    c_list = sorted([s.count(x) for x in set(s)])
    
    for num in m_list:
        if c_list == sorted([num.count(x) for x in set(num)]):
            return int(num)
    
    return -1
            
print(solution("ab")) # 81
print(solution("zzz")) # -1