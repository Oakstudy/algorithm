function solution(ml, text) {
    let arr = text.split(' ');
    let cnt = 0;
    arr.map( x => {
        const match = x.match(/[a-zA-Z]+/g);
        match && (match[0]).length <= ml ? cnt++ : null
    });
    return cnt
}

function solution2(maxLength, text) {
    return (text.match(/\w+/g) || []).filter(elm => elm.length <= maxLength).length
}

console.log(solution(4, "The Fox asked the stork, 'How is the soup?'")); // 7
console.log(solution(1, "...")); // 0
console.log(solution(3, "This play was good for us.")) // 3