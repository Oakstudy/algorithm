package main

import (
	"fmt"
)


func solution(inputArray []int) int {
	result := 0
	for _, v := range inputArray {
		if v == 0 {
			break
		}
		result += v
	}
	return result
}


func main() {
	fmt.Println(solution([]int{5, 1, 2, 3, 0, 1, 5, 0, 2}))
}