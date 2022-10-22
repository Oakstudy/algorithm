function solution(coins, price) {
    let result = 0;
    coins.sort((a, b) => b-a).map(x => {
            result += ~~(price / x)
            price %= x
        })
    return result;
}

console.log(solution([1,5,10,100], 239))
