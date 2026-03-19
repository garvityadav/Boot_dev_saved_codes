package main

func getMaxMessagesToSend(costMultiplier float64, maxCostInPennies int) int {
	actualCostInPennies := 1.0
	maxMessagesToSend := 0
	balance := float64(maxCostInPennies) - actualCostInPennies
	for {
	if balance < 0 {
		break
	}
		actualCostInPennies *= costMultiplier
		balance -= actualCostInPennies
		maxMessagesToSend++

	}


	return maxMessagesToSend
}

