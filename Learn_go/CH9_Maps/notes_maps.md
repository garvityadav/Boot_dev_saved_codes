# Maps

to declare a map : 
```go
newMap := make(map[string]int)
newMap["Alice"]= 1235123112
// or using literal:
newMap:=map[string]int{
    "Alice":1235123112,
}

// The len function also works in maps
fmt.Println(len(newMap)) // 1
```

## Mutation

```go 
// Insert a key
newMap[key] = element

// Get a key
element = newMap[key]

// delete an element
delete(newMap,key)

// check if key exist 
element , ok := newMap(key) // if found , ok returns true and the value will be in element    


```
