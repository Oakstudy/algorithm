function solution(a) {
    return a.map((x, i) => {
        let acc = 0;
        for (let j = i; j < a.length; j++) acc += a[j];
        return (acc %2 === 0) ? x : Math.abs(x-1);
    })
}

function solution2(a) {
    let num = a.reduce((a,b)=> a+b,0)
    return a.map(elm => {
      if(elm === 1) num -=1
      return num%2
    })
  }

function solution3(a) {
    for (let i = 0; i < a.length; i++) {
        if (a[i]) {
            for (let j = 0; j <= i; j++) {
                a[j] = !a[j] * 1;
            }
        }
    }
    return a;
}


console.log(solution([1, 1, 1, 1, 1])) // [0, 1, 0, 1, 0]