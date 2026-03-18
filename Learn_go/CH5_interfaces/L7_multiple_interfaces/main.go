package main
import (
"fmt"
"unicode/utf8"
)

func (e email) cost() int {
	totalCost := 0
	if e.isSubscribed==false{
	totalCost = utf8.RuneCountInString(e.body)*5	
}else{
	totalCost = utf8.RuneCountInString(e.body)*2
}
	return totalCost
}
func (e email) format() string {
	message:=fmt.Sprintf("'%s' | Subscribed",e.body)
	if e.isSubscribed == false{
	message = fmt.Sprintf("'%s' | Not Subscribed",e.body)
}
	return message
}

type expense interface {
	cost() int
}

type formatter interface {
	format() string
}

type email struct {
	isSubscribed bool
	body         string
}

