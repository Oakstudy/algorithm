def solution(coins, price):
    result = 0
    for coin in coins[::-1]:
        result += (price // coin)
        price %= coin
    return result

def solution2(coins, price):
    res = 0
    for coin in reversed(coins):
        t, price = divmod(price, coin)
        res += t
    return res


print(solution([1,5,10,100], 239))