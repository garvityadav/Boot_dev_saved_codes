package main

func bulkSend(numMessages int) float64 {
	sum :=0.0
	for i:=0;i<numMessages;i++{
		sum+=1+(0.01*float64(i))
}	
	return sum
}

