package main

import "fmt"

func solution(legs int) []int {
	arr := make([]int, 0)
	for legs >= 0 {
		arr = append(arr, legs / 2)
		legs -= 4
	}
	result := make([]int, 0)
	for i := len(arr)-1; i>=0; i-- {
		result = append(result, arr[i])
	}
	return result
}

func main() {
	for _, v := range []int{6, 2, 8, 4} {
		fmt.Println(solution(v))
	}
}