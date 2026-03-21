package main

func getMessageCosts(messages []string) []float64 {
	finalCostMessageSlice:=make([]int,len(messages))
	finalCostSlice:=make([]float64,len(messages))	
	for i:=0;i<len(finalCostMessageSlice);i++{
		finalCostSlice[i]= float64(len(messages[i])) * 0.01
	}
	return finalCostSlice
}


