def solution(startTag):
    first = startTag.split(' ')[0]
    return f"</{first[1:]}{ '>' if first[-1] != '>' else ''}"


print(solution("<button type='button' disabled>"))
print(solution("<i> type='button' disabled"))