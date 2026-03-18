## Interface
An interface helps us foucs on what a type does rather than how it's built. 
Interfaces are just collection of methods signatures. A type implements an interface if it has methods that matches the interface's method signatures. 
struct is noun and interface is the verb
Struct shows the data and interface creates the action.
for example : 

```go
// I have a shape interface
type shape interface{
    area() float64
    parameter float64
}
type rectangle struct{
    length float64
    breadth float64
}

func (r rectangle) area() float64{
    return r.length * r.breadth
}

// here i will use the interface 
box := rectange{23,28}
fmt.Println(box.area()) // this will print the area for the box
```

## Multiple Interfaces
A single interface could be implemented by multiple structs. To find out which struct implements the interface , we check it using functions. 

for example 
```go
type count interface{
    wheelsCount()
}

type car struct{
    colour string
    engineCC int
}

type plane struct{
    
    hoseLength int
}
```
To implement the interface in both the structs : 
```go
func (c car) 
``` 
