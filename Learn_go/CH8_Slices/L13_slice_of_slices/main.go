package main

func createMatrix(rows, cols int) [][]int {
	resultMatrix := [][]int{}
	for i:=0;i<rows;i++{
		subSlice:=make([]int,0,cols)
		for j:=0;j<cols;j++{
			subSlice = append(subSlice,i*j)	
		}
		resultMatrix = append(resultMatrix,subSlice)	
	}
	
	return resultMatrix
}

