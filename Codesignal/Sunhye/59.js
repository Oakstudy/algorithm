function solution(a, b) {
    var count = 0;
    while(true){
        for(let char of a){
            if(b.indexOf(char) < 0){
                return count;
            }
            b = b.replace(char, "");
        }
        count ++;
        
    }
    return count;

}