# Arrays 

In golang , arrays are the same as list in python. They have immutable length , yet we can mutate the elements inside the length. 

## Slices 
Slices are the golang way to mutate arrays. When we use slice , we are essentially creating a window for array. 
The struct of slice looks like this: 
```go
type slice struct {
    array unsafe.Pointer  // piointer to the underlying array
    length int              // current length of the slice
    capacity int            // capacity of the underlying array
}
```

## Functionality of slices. 

### How does we add elements in the array ?
So if we want to append elements or a whole array to the array , go does something different. 
As we know that array's length is fixed , we can't expand so when we want to append we do via slice, **append()** method helps do that.
**Append**:
    - Function signature :
        ```go
         func append(slice []Type,elems ...Type)[]Type
        ```
    - using make() , it looks for the current capacity:
        - if current capacity  < 256 elements , go will double the capacity.
        - if capacity >256 , go will transition to a formula where : 
            - go will grow the capacity to roughly 1.25x or 1.25(x)+0.75xthreshold
        - it copyies the old elements into the slice. 
    - At last it appends all the new elements one by one to the new slice and returns it.
    
### Make 
Make is a function which helps us creating a new slice : 

```go
newSlice := make([]int,length int ,capacity int)

// capacity is generally not needed
newSliceB := make([]int, length)
```
    
### Variadic 
We can use ... to spread the array for an argument in a function. Example : 
```go 
func printStrings(strings ...string)string {
    for i:=0;i<len(structs);i++{
        fmt.Println(strings[i])
}
}
func main(){
    names:= []string{"bob","sue","alice"}
    printStrings(names...)
}
```
### Range 
Go provides a syntactic sugar to iterate a slice: 
```go
for INDEX, ELEMENT:= range SLICE{
}
```
The element is the item which is indexed. 

For example : 
```go 
fruits := []string{"apple","banana","oranges"}
for i,fruit:= range fruits{
    fmt.Println(i,fruit)
}
```

