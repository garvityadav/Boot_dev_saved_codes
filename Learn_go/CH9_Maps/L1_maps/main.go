package main

import "errors"

func getUserMap(names []string, phoneNumbers []int) (map[string]user, error) {
	users:=make(map[string]user)
	if len(names) !=len(phoneNumbers){
		return users,errors.New("invalid sizes")
	}	
	for i := range names{
		element := user{
			name : names[i],
			phoneNumber: phoneNumbers[i],
		}	
		users[names[i]]=element
	}
	return users,nil
}

type user struct {
	name        string
	phoneNumber int
}

