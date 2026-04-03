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

## Pointer Receivers
A receiver type of a method can be a pointer. 
Method with pointer receive can change the value of which the receiver points.

For example : 
```go
type car struct {
  color string
}

func (c *car) setColor(color string){
  c.color = color
}

func main (){
  c :=car {
    color : "white"
  }
  c.setColor("blue")
  fmt.println(c.color)
  // prints blue
}
```

But when passed value 
```go
type car struct {
  color string
}

func (c car) setColor(color string){
  c.color = color
}

func main (){
  c :=car {
    color : "white"
  }
  c.setColor("blue")
  fmt.println(c.color)
  // prints white
}
```

Pointer receiver are used widely in go. 


