def solution(address):
    num = len(address) - address[::-1].find("@")
    return address[num:]

def solution(address):
    return address.split('@')[-1]

def solution(address):
    return address[address.rfind('@')+1:]


print(solution("prettyandsimple@example.com"))
print(solution("fully-qualified-domain@codesignal.com"))
print(solution("\"very.unusual.@.unusual.com\"@usual.com"))
