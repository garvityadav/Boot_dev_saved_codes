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
## key Types:

Keys in map are of any type which are comparable. In go compareable types are : 
1. Boolean,
2. string,
3. numeric,
4. pointer,
5. Channel,
6. Interface type.

To create a map of string which is a mapt of string as key and int as value, we:

```go 
hits:=make(map[string]map[string]int)
```

but to create the above map , we have to check wether the internal map exist (map[string]int). 

```go 
func add(m map[string]map[string]int,path,country string){
    mm,ok:=m[path]
    if !ok == true{
       mm= make(map[string]int)
        m[path] = mm 
    }
    mm[country]++
}
add(hits,"/doc/","au")
```
But the above gets tedious very easily , so ,

```go 
type Key struct{
    Path,Country string
}
hits:=make(map[Key]int)

// to add 
hits[Key{"/","vn"}]++ 

//to get
n:= hits[Key{"/ref/spec","ch"}]
```
