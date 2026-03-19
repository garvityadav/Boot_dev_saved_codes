package main

func countConnections(groupSize int) int {
	sum :=0
	for i:=1;i<=groupSize;i++{
		sum+=i-1	
	}
	return sum
}

