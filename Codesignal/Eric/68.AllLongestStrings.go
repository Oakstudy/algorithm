package main

import "fmt"

func solution(input []string) []string {
	longestLength := 0
	for _, str := range input {
		if len(str) > longestLength {
			longestLength = len(str)
		}
	}
	result := []string{}
	for _, str := range input {
		if len(str) == longestLength {
			result = append(result, str)
		}
	}
	return result
}

func main() {
	result := solution([]string{"aba", "aa", "ad", "vcd", "aba"})
	fmt.Println(result)
}

