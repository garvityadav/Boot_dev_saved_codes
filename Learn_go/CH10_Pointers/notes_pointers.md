# Pointers 
These are variables which points to the actual memory where the data is stored. 

For example : 
```go 
myString := "hello"
myStringPtr := &myString
```

To initiate a nil pointer we use : 
```go 
var p *int
```
```

Instead of starting as a nil pointer, its common to use & operator to get a pointer to its operand.

```go 
myString:= "hello"
myStringPtr:= &myString
```
```
```

## Dereference

The * operator Dereferences to a pointer to get the original value.

```go
*myStringPtr = "world"
fmt.Printf("value of myString:%s\n",*myStringPtr)
```
```
```
