package main

func getMessageWithRetries(primary, secondary, tertiary string) ([3]string, [3]int) {
	// cost of each message  = cost of previous message + current 
	finalMessage:=[3]string{primary,secondary,tertiary}
	finalCost:=[3]int{len(primary),len(primary)+len(secondary),len(primary)+len(secondary)+len(tertiary)}
	return finalMessage,finalCost
}

