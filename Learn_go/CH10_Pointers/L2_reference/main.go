package main

import "strings"

func removeProfanity(message *string) {
	words := map[string]string{
		"fubb":  "****",
		"shiz":  "****",
		"witch": "*****",
	}
	for word, replacement := range words {
		*message = strings.ReplaceAll(*message, word, replacement)
	}
}
