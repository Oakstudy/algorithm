package main

import (
	"fmt"
)

func solution(a []int) []int {
	result := make([]int, 0)
	for i, v := range a {
		acc := 0
		for j := i; j < len(a); j++ {
			acc += a[j]
		}
		val := v
		if acc%2 == 1 {
			val = v - 1
			if val < 0 {
				val = 1
			}
		}

		result = append(result, val)
	}
	return result
}

func main() {
	fmt.Println(solution([]int{1, 1, 1, 1, 1})) // [0,1,0,1,0]
}
