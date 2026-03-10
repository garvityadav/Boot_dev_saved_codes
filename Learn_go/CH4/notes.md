# Why Golang ? 
It creates machine readable code. So you just have to compile once and then that code can be used on any machine regardless it has go installed or not. 

#### How is it better than JS or Python ? Why should we choose it over these ? 

## Structs

### What is struct? 
Struct (structure in short) is a custom data type which we can use to define combination of datatypes for our program. For example : 
```go
type car struct{
    wheels int
    colour string
}
``` 
To use these struct, dot notation is used.


### Nested Struct
A nested struct is a struct inside another struct. For example: 
```go
type car struct{
    frontwheel wheel 
    backwheel wheel
    colour string
    engine string
}

type wheel struct{
    radius int 
    material string
}

myCar := car{}
myCar.frontWheel.radius = 5
```

### Anonymus structs 
Anonymus structs are used when the struct will only be used once or in a limit. These structs are created instantly and used instantly. 
For example : 
```go
myVisorColor:= struct{
   color string 

}{
    color: "Green"
}

```


### Embeded Structs
Embeded struct are used to embedd structs and their fields can be used at the top level like normal fields.
For example: 
```go
type car struct{
    brand string,
    model string
}

type truck struct{
    bedSize int
    car

}

myTruck := truck{
    bedSize : 10,
    car:car{
    brand : "Toyota",
    model : "L1"
},
}
fmt.Println(myTruck.brand)
fmt.Println(myTruck.model)
```

