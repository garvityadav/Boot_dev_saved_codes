package main

func getLast[T any](s []T) T {
	var lastElem T
	if len(s) <= 0 {
		return lastElem
	}
	lastElem = s[len(s)-1]
	return lastElem
}
