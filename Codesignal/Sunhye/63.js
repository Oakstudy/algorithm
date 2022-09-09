function solution(a) {
    let groups = new Set(), i;
    for (i = 0; i < a.length; i++)
        groups.add(Math.ceil(1e-4 * a[i]));
        console.log(groups);
    return groups.size + a.length; 
}
