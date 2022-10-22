// function solution(s) {
//     for (let i=0; i<s.length-1; i++) {
//         if (s[i] >= s[i+1]) return false;
//     }
//     return true;
// }

function solution2(s) {
    return [...new Set(s)].sort().join('') === s;
}

console.log(solution2('effg')); // false