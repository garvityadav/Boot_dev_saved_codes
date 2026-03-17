package main

type notification interface {
	importance() int
}

type directMessage struct {
	senderUsername string
	messageContent string
	priorityLevel  int
	isUrgent       bool
}

type groupMessage struct {
	groupName      string
	messageContent string
	priorityLevel  int
}

type systemAlert struct {
	alertCode      string
	messageContent string
}


func (d directMessage) importance() int{
	if d.isUrgent{
	return 50
}
	return d.priorityLevel
}

func (g groupMessage) importance() int{
	return g.priorityLevel
}

func (s systemAlert) importance() int{
	return 100
}


func processNotification(n notification) (string, int) {
	switch notificationVal := n.(type){
	case directMessage:
		return notificationVal.senderUsername,notificationVal.importance()
	case groupMessage:
		return notificationVal.groupName,notificationVal.importance()
	case systemAlert:
		return notificationVal.alertCode,notificationVal.importance() 
	default:
		return "",0
}
}

