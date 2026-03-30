package main

import (
	"strings"
)

func countDistinctWords(messages []string) int {
	hashMap := make(map[string]struct{})
	for _, message := range messages {
		for word := range strings.FieldsSeq(message) {
			word = strings.ToLower(word)
			hashMap[word] = struct{}{}
		}
	}
	return len(hashMap)
}
