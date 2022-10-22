package main

import "fmt"

func solution(picture []string) []string {
	star := "*"
	for i := 0; i < len(picture[0])+1; i++ {
		star += "*"
	}
	result := []string{star}
	for i := 0; i < len(picture); i++ {
		result = append(result, "*" + picture[i] + "*")
	}
	result = append(result, star)
	return result
}

func main() {
	fmt.Println(solution([]string{"abc", "ded"}))
}