function solution(string1, string2) {

	for (let i = 0; i < string1.length; i++) {
		let firstInx1 = string1.indexOf(string1[i]);
		console.log(firstInx1);
		let firstInx2 = string2.indexOf(string2[i]);
		//console.log(firstInx2);
		if ((string2[firstInx1] !== string2[i]) || (string1[firstInx2] !== string1[i])) return false;
	}
	return true;
}
