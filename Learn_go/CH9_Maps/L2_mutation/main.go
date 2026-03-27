package main
import 	(
	"errors"
	)

func deleteIfNecessary(users map[string]user, name string) (deleted bool, err error) {
	isUserExist , ok := users[name]
	if ok==false{
		return false,errors.New("not found")
	}
	if isUserExist.scheduledForDeletion == false{
		return false,nil
	}else{
		delete(users,name)
		return true,nil
	}
}

type user struct {
	name                 string
	number               int
	scheduledForDeletion bool
}

