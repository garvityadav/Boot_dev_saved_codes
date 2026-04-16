package main

func countReports(numSentCh chan int) int {
	sum := 0
	for {
		num, ok := <-numSentCh
		if !ok {
			break
		}
		sum += num
	}
	return sum
}

// don't touch below this line

func sendReports(numBatches int, ch chan int) {
	for i := 0; i < numBatches; i++ {
		numReports := i*23 + 32%17
		ch <- numReports
	}
	close(ch)
}
