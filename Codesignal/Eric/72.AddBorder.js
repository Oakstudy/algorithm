function solution(pic) {
    const stars = '*'.repeat(pic[0].length + 2);
    let list = [];
    list.push(stars);
    pic.map (x => list.push('*' + x + '*'));
    list.push(stars);
    return list
}


function solution2(pic) {
    return [x='*'.repeat(pic[0].length + 2), ...pic.map(x => '*' + x + '*'), x]
}

console.log(solution2(["abc", "ded"]))