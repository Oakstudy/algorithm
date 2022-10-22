package main

import "fmt"

func solution(coins []int, price int) int {
	result := 0
	for i := len(coins) - 1; i >= 0 ; i-- {
		result += price / coins[i]
		price %= coins[i]
	}
	return result
}

func main() {
	fmt.Println(solution([]int{1, 5, 10, 100}, 239));
}