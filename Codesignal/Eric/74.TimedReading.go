package main

import (
	"fmt"
	"strings"
	"regexp"
)


func solution(ml int, text string) int {
	arr := strings.Split(text, " ")
	re := regexp.MustCompile(`[a-zA-Z]+`)
	count := 0
	for _, v := range arr {
		match := string((re.Find([]byte(v)))[:])
		if 0 < len(match) && len(match) <= ml {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(solution(4, "The Fox asked the stork, 'How is the soup?'")) // 7
	fmt.Println(solution(1, "...")) // 0
}