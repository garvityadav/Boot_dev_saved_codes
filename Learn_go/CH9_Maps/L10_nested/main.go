package main

func getNameCounts(names []string) map[rune]map[string]int {
	finalMap := make(map[rune]map[string]int)
	for _, name := range names {
		key := []rune(name)[0]
		if _, ok := finalMap[key]; !ok {
			finalMap[key] = make(map[string]int)
		}
		finalMap[key][name]++
	}
	return finalMap
}
