function solution(s) {
    let max = 0;
 let obj1 = {};
 s.split('').map(a=>obj1.hasOwnProperty(a) ? obj1[a]++ : obj1[a] = 1)
 for(let i = 3; Math.pow(i, 2).toString().length <= s.length; i++){
   let temp = Math.pow(i, 2);
   let obj2 = {};
   temp.toString().split('').map(a=>obj2.hasOwnProperty(a) ? obj2[a]++ : obj2[a] = 1)
   if(Object.keys(obj1).length === Object.keys(obj2).length && temp.toString().length === s.length && temp > max){
     let arr1 = []
     let arr2 = []
     for(key in obj1){
       arr1.push(obj1[key])
     }
     for(key in obj2){
       arr2.push(obj2[key])
     }
     if(arr1.sort((a,b)=>a-b).join('') === arr2.sort((a,b)=>a-b).join('')){
       max = temp
     }
   }
 }
 return max > 0 ? max : -1
 }
 