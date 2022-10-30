function solution(votes, k) {
    let result = 0;
    votes.sort((a,b) => a-b);
    for (let i = 0; i < votes.length-1; i++) {
        if (votes[i] + k > votes[votes.length-1]) {
            result = votes.length - i;
            break;
        }
    }
    if (result === 0 && votes[votes.length-1] !== votes[votes.length-2]) {
        result = 1;
    }
    return result;
}

function solution2(votes, k) {
    max = Math.max(...votes)
    return k ? votes.filter(x => x+k > max).length : votes.filter(x => x==max).length == 1 ? 1 : 0
}


// console.log(solution([2, 3, 5, 2], 3)); // 2
console.log(solution([1, 1, 1, 1], 1)); // 4