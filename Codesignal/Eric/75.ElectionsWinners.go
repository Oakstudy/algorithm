package main

import (
	"fmt"
	"sort"
)


func solution(votes []int, k int) int {
	sort.Ints(votes)
	result := 0
	for i, v := range votes {
		if v+k > votes[len(votes)-1] {
			result = len(votes) - i
			break
		}
	}
	if result == 0 && votes[len(votes)-1] != votes[len(votes) - 2] {
		result =1
	}
	return result
}


func main() {
	fmt.Println(solution([]int{2, 3, 5, 2}, 3)) // 2
	fmt.Println(solution([]int{1, 3, 3, 1, 1}, 0)) // 0
	fmt.Println(solution([]int{5, 1, 3, 4, 1}, 0)) // 1
	fmt.Println(solution([]int{1, 1, 1, 1}, 1)) // 4
	fmt.Println(solution([]int{1, 1, 1, 1}, 0)) // 0
	fmt.Println(solution([]int{3, 1, 1, 3, 1}, 2)) // 2
}