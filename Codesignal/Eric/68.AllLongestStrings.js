function solution(input) {
    sorted = [...input]
    sorted.sort((a, b) => a.length - b.length);
    const length = sorted[sorted.length - 1].length;
    return sorted.filter((item) => item.length === length);
}

console.log(solution(["a", 
"abc", 
"cbd", 
"zzzzzz", 
"a", 
"abcdef", 
"asasa", 
"aaaaaa"]))